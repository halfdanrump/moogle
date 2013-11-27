#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python csv file reader

import glob

def createClinicDict(header_list,item_list):

	clinic_dict = {}

	for i in range(len(header_list)):
		for j in range(len(header_list[i])):

			print header_list[i],item_list[i]
			


def csvReader(csv_file):

	import csv
	item_list = []
	with open(csv_file) as csvin:
		csvin = csv.reader(csvin)
		for row in csvin:
			print row
			item_list.append(row)
		
		print item_list	
		return item_list

def readData(header,data):

	item_list = []
	header_list = []

	for i in range(len(header)):
		#print header[i]#,data[i]
		header_list.append(csvReader(header[i])[0])
		item_list.append(csvReader(data[i])[0])
	
	return header_list,item_list

if __name__ == '__main__':

	header_file = glob.glob('../../db/csv/headers/*.csv')
	data = glob.glob('../../db/csv/data/*.csv')

	header_list,item_list = readData(header_file,data)
	createClinicDict(header_list,item_list)
