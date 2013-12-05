import csv
data_path = '../../db/csv/data/'
header_path = '../../db/csv/headers/'
import pandas
import psycopg2

def read_boolean_data(header_file, data_file):
	full_header_path = header_path + header_file
	full_data_path =  data_path + data_file

	header = open(full_header_path).read().split(',')
	header = [h.replace('"', '') for h in header]

	data = pandas.io.parsers.read_csv(full_data_path, header = 0, names = header)
	c_id = data.ix[:,0]

	n_rows = data.shape[0]
	n_columns = data.shape[1]
	
	c_codes = data.iloc[:,0]
	misc = data.iloc[:,n_columns-1]

	data = data.drop(data.columns[n_columns-1], 1)
	data = data.drop(data.columns[0], 1)
	
	c_dict = dict()

	for (i, row),(j, m) in zip(data.iterrows(), misc.iteritems()):
		items = list()
		for c, cell in enumerate(row):
			if cell == True: items.append(data.columns[c])
		if not str(m) == 'nan':
			items.append(m)
		c_dict[c_codes[i]] = " ".join(items)
	return c_dict


def make_fulldoc(column_dict, cursor):
	max_n_clinics = 0
	for column_name, data_dict in column_dict.items():
		if len(data_dict.keys()) > max_n_clinics:
			max_n_clinics = len(data_dict.keys())
			largest_dict = data_dict


	c_codes = largest_dict.keys()
	print c_codes
	for code in c_codes:
		print code
		row = list()		
		for column_name, data_dict in column_dict.items():
			try:
				print column_name
				row.append(data_dict[code])
				print data_dict[code]
			except KeyError:
				pass
		full_doc = " ".join(row)
		query = "INSERT INTO fulldocs(doc) VALUES ('%s')" % (full_doc)	
		cursor.execute(query)
	




def store_all_columns():
	all_columns = dict()
	all_columns['departments'] = read_boolean_data('B_02_shinsatsu_header.csv', 'B_02.csv')
	all_columns['machines'] = read_boolean_data('B_10_shinryoukiki_header.csv', 'B_10.csv')
	conn = psycopg2.connect("dbname=moogle host=localhost user=moogle")
	cursor = conn.cursor()
	make_fulldoc(all_columns, cursor)
	conn.commit()
	cursor.close()

if __name__ == "__main__":
	#conn = psycopg2.connect("dbname=moogle host=localhost user=moogle")
	#cursor = conn.cursor()
	store_all_columns()