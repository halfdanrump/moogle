#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python csv file reader

import glob


def csvReader(csv_file):

	import csv
	item_list = []
	with open(csv_file) as csvin:
		csvin = csv.reader(csvin)
		for row in csvin:
			item_list.append(row)
		
		print item_list	
		return item_list

def readData(header,data):

	item_list = []
	header_list = []

	for i in range(len(header)):
		#print header[i],data[i]
		items = []
		
		header_list = header_list + csvReader(header[i])[0]
		items = items+csvReader(data[i])
		print items

		item_list.append(items)
	
	return header_list,item_list

if __name__ == '__main__':

	header_file = glob.glob('../../db/csv/headers/*.CSV')
	data = glob.glob('../../db/csv/data/*.CSV')

	header_list,item_list = readData(header_file,data)
	
