import pandas
import psycopg2

data_path = '../../db/csv/data/'
header_path = '../../db/csv/headers/'

def store_dictionary_as_row_in_database(cursor, dictionary):
	for column, data in dictionary:
		query = "INSERT INTO fulldocs(%s) VALUES ('%s')" % (column, data)	
		cursor.execute(query)

def read_csv(header_file, data_file):
	full_header_path = header_path + header_file
	full_data_path =  data_path + data_file

	header = open(full_header_path).read().split(',')
	header = [h.replace('"', '') for h in header]

	data = pandas.io.parsers.read_csv(full_data_path, header = 0, names = header)
	#c_id = data.ix[:,0]
	
	#n_rows = data.shape[0]
	n_columns = data.shape[1]
	print n_columns
	c_codes = data.iloc[:,0]
	misc = data.iloc[:,n_columns-1]

	data = data.drop(data.columns[n_columns-1], 1)
	data = data.drop(data.columns[0], 1)	
	return c_codes, data, misc

def read_boolean_data(header_file, data_file):
	c_codes, data, misc = read_csv(header_file, data_file)

	c_dict = dict()

	for (i, row),(j, m) in zip(data.iterrows(), misc.iteritems()):
		items = list()
		for c, cell in enumerate(row):
			if cell == True: items.append(data.columns[c])
		if not str(m) == 'nan':
			items.append(m)
		c_dict[c_codes[i]] = " ".join(items)
	return c_dict

def read_data_as_is(header_file, data_file, rightmost_column = 10):
	c_codes, data, misc = read_csv(header_file, data_file)
	data = data[data.columns[0:rightmost_column]]
	c_dict = dict()
	for code, (i, row) in zip(c_codes, data.iterrows()):
		row_dict = dict()
		for c, cell in enumerate(row):
			row_dict[data.columns[c]] = cell
		c_dict[code] = row_dict
	return c_dict

def make_fulldoc(column_dict, cursor):
	max_n_clinics = 0
	### Pick list with the most clinics
	for column_name, data_dict in column_dict.items():
		if len(data_dict.keys()) > max_n_clinics:
			max_n_clinics = len(data_dict.keys())
			largest_dict = data_dict

	### Iterate over list with most clinics and collect data for each clinics from the various dictionaries
	c_codes = largest_dict.keys()
	for code in c_codes:
		print code
		row = list(code)		
		for column_name, data_dict in column_dict.items():
			print column_name
			try:
				row.append(data_dict[code])
			except KeyError:
				pass
		full_doc = " ".join(row)
		query = "INSERT INTO fulldocs(doc) VALUES ('%s')" % (full_doc)	
		cursor.execute(query)
	




def store_all_columns():
	all_columns = dict()
	print read_data_as_is('B_01_byouin_header.csv', 'B_01.csv', rightmost_column = 22)
	#all_columns['departments'] = read_boolean_data('B_02_shinsatsu_header.csv', 'B_02.csv')
	#all_columns['facilities'] = read_boolean_data('B_03_iryo_header.csv', 'B_03.csv')
	#all_columns['machines'] = read_boolean_data('B_10_shinryoukiki_header.csv', 'B_10.csv')

	conn = psycopg2.connect("dbname=moogle host=localhost user=moogle")
	cursor = conn.cursor()
	#make_fulldoc(all_columns, cursor)
	conn.commit()
	cursor.close()

if __name__ == "__main__":
	#conn = psycopg2.connect("dbname=moogle host=localhost user=moogle")
	#cursor = conn.cursor()
	store_all_columns()
