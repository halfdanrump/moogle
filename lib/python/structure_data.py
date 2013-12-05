import csv
data_path = '../../db/csv/data/'
header_path = '../../db/csv/headers/'
import pandas
def read_machines_data():

	machines_header_path = header_path + 'B_10_shinryoukiki_header.csv'
	machines_data_path = data_path + 'B_10.csv'
	
	header = open(machines_header_path).read().split(',')
	header = [h.replace('"', '') for h in header]
	
	machines_data = pandas.io.parsers.read_csv(machines_data_path, header = 0, names = header)
	c_id = machines_data.ix[:,0]

	n_rows = machines_data.shape[0]
	n_columns = machines_data.shape[1]
	
	c_codes = machines_data.iloc[:,0]
	machines_data = machines_data.drop(machines_data.columns[0], 1)
	
	c_dict = dict()

	for i, row in machines_data.iterrows():
		machines = list()
		for c, cell in enumerate(row):
			if cell == True: machines.append(machines_data.columns[c])
		c_dict[c_codes[i]] = ", ".join(machines)

	return c_dict

if __name__ == "__main__":
	read_machines_data()