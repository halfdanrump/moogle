#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python MySQL tsv uploader

import csv
import psycopg2
import sys
csv.field_size_limit(sys.maxsize)

def tsvReader(tsv_file):

    item_list = []

    with open(tsv_file) as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')

        for row in tsvin:
            #print row
            item_list.append(row)

    return item_list

def insertPostgres(item_list):

	conn = psycopg2.connect("dbname=moogle host=localhost user=moogle")
	cursor = conn.cursor()

	column_name = item_list[0]
	for row in item_list[1:]:
		#print row
		for i in range(len(row)):

			if row[i] == '':
				row[i] == None
			else:
				try:
					row[i] = int(row[i])	
				except:
					pass
				#print row[i], type(row[i])

		
		#query = u"INSERT INTO test2(id,service_id,item_code,name,url,comment,category,area,price,stock_flg,img_url,count,norm,last_update,fixed,final_weight,created_at,mb_name,mb_comment,mb_url,mb_img_url) VALUES ('%s','%d','%s','%s','%s','%s','%s','%d','%d','%d','%s','%d','%s','%s','%d','%s','%s','%s','%s','%s','%s')" % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20])
		try:
			query = u"INSERT INTO item_masters(id,service_id,item_code,name,url,comment) VALUES ('%s','%d','%s','%s','%s','%s')" % (row[0],row[1],row[2],row[3],row[4],row[5])	
			print query
			cursor.execute(query)
			mydb.commit()
		except:
			pass
	cursor.close()

if __name__ == '__main__':
	argvs = sys.argv
	item_file = argvs[1]
	item_list = tsvReader(item_file)
	
	insertPostgres(item_list)
