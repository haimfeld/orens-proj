# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:20:35 2017

@author: Haim
"""

import pymysql

import pymysql.cursors
conn= pymysql.connect(
        host='localhost',
        user='root',
        password='9246865',
        db='licence_plate_proj')
#        )



a=conn.cursor()
a.execute("SELECT * FROM car_num_names")


print(a.description)


for row in a:
    print (row)


#a.execute(sql)


