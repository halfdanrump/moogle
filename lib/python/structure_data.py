import pandas
import psycopg2
import sys
data_path = '../../db/csv/data/'
header_path = '../../db/csv/headers/'




def read_csv(header_file, data_file):
	full_header_path = header_path + header_file
	full_data_path =  data_path + data_file

	header = open(full_header_path).read().split(',')
	header = [h.replace('"', '') for h in header]

	data = pandas.io.parsers.read_csv(full_data_path, header = 0, names = header)
	#c_id = data.ix[:,0]
	
	#n_rows = data.shape[0]
	n_columns = data.shape[1]
	#print n_columns
	c_codes = data.iloc[:,0]
	misc = data.iloc[:,n_columns-1]

	data = data.drop(data.columns[n_columns-1], 1)
	data = data.drop(data.columns[0], 1)	
	return c_codes, data, misc

def read_boolean_data(column_name, header_file, data_file):
	c_codes, data, misc = read_csv(header_file, data_file)

	c_dict = dict()

	for (i, row),(j, m) in zip(data.iterrows(), misc.iteritems()):
		items = list()
		for c, cell in enumerate(row):
			if cell == True: items.append(data.columns[c])
		if not str(m) == 'nan':
			items.append(m)
		c_dict[c_codes[i]] = {column_name:" ".join(items)}
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

def merge_all_dicts(list_of_dicts):
	max_n_clinics = 0
	### Pick list with the most clinics
	for data_dict in list_of_dicts:
		if len(data_dict.keys()) > max_n_clinics:
			max_n_clinics = len(data_dict.keys())
			largest_dict = data_dict
	
	c_codes = largest_dict.keys()
	all_rows = list()
	for code in c_codes:
		#print code
		row_dict = {'code':code}
		for data_dict in list_of_dicts:
			if data_dict.has_key(code):
				for column, content in data_dict[code].items():
					#print column
					row_dict[column] = content
		all_rows.append(row_dict)
	return all_rows



def read_all_files():
	all_dicts = list()
	
	all_dicts.append(read_data_as_is('B_01_byouin_header.csv', 'B_01.csv', rightmost_column = 22))
	all_dicts.append(read_boolean_data('departments', 'B_02_shinsatsu_header.csv', 'B_02.csv'))
	all_dicts.append(read_boolean_data('facilities', 'B_03_iryo_header.csv', 'B_03.csv'))
	all_dicts.append(read_boolean_data('machines', 'B_10_shinryoukiki_header.csv', 'B_10.csv'))
	return all_dicts
	

	
	#make_fulldoc(all_columns, cursor)


def store_all_rows(cursor, merged_dicts):
	
	for i, row_dict in enumerate(merged_dicts):
		print i
		#for i, (column_name, value) in enumerate(row_dict.items()):
		#	query = "INSERT INTO fulldocs(%s) VALUES ('%s')" % (column_name.upper(), value)	
		#	print query
		#	#cursor.execute(query)
		#for i, (column_name, value) in enumerate(row_dict.items()):
		full_doc = ','.join([str(v) for v in row_dict.values()])
		columns = ','.join(row_dict.keys()) + ',doc'
		values = "'" + "','".join([str(v) for v in row_dict.values()]) + "','%s'"%full_doc
		query = "INSERT INTO fulldocs(%s) VALUES (%s)" % (columns, values)
		print query
		cursor.execute(query)

def transfer_all_data():	
	conn = psycopg2.connect("dbname=moogle host=localhost user=moogle")
	cursor = conn.cursor()
	all_dicts = read_all_files()
	merged_dicts = merge_all_dicts(all_dicts)
	store_all_rows(cursor, merged_dicts)
	#return all_dicts, merged_dicts
	conn.commit()
	cursor.close()

if __name__ == "__main__":
	transfer_all_data()