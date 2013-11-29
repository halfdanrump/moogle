#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python csv file reader

import glob

def createClinicDict(header_list,item_list):

	clinic_dict = {}

	for file_num in range(len(header_list)):
		for clinic_num in range(len(header_list[file_num])):
			print item_list[file_num][clinic_num]


def csvReader(csv_file):

	import csv
	item_list = []
	with open(csv_file) as csvin:
		csvin = csv.reader(csvin)
		for row in csvin:
			#print row
			item_list.append(row)
		
		item_len = len(item_list)
		return item_list

def readData(header,data):

	item_list = []
	header_list = []

	for i in range(len(header)):

		items = []
		header_list = header_list + csvReader(header[i])[0]
		csv_list = csvReader(data[i])
		print len(csv_list)
		for d in range(len(csv_list)):
			item_list.append([])
			item_list[d].append(csv_list[d])

		#item_list.append(items)

	#item_data = [i for s for i in item_list]
	
	return header_list,item_list

if __name__ == '__main__':

	header_file = glob.glob('../../db/csv/headers/*.csv')
	data = glob.glob('../../db/csv/data/*.csv')

	header_list,item_list = readData(header_file,data)
	#createClinicDict(header_list,item_list)
