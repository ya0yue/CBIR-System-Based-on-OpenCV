# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:31:51 2017

@author: Mars
"""

import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","sys" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * from sys.path_table")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()
print data
#print ("Database version : %s " % data)

# 关闭数据库连接
db.close()
