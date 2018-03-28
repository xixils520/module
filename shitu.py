import json
import requests
import pymysql
session=requests.Session()
db = pymysql.connect(host='192.168.1.101', port=3306, user='dddev', passwd='123456', db='ctcdb_reconciliation',
                     charset='utf8')
good_sql='SELECT DISTINCT(goods_id) FROM `io_stock_view` where warehouse_Id=10'
cursor=db.cursor()
cursor.execute(good_sql)
cursor.close()
results=cursor.fetchall()
list1=[]
for row in results:
    row=row[0]
    list1.append(row)
for goods_id in list1:
    sql_1='SELECT id,warehouse_Id,goods_id,begin_num,end_num,createdAt FROM `io_stock_view` WHERE warehouse_Id=10 AND goods_id=%s AND createdAt >"2018-03-25 00:00:00" ORDER BY createdAt'%goods_id
    cursor1=db.cursor()
    cursor1.execute(sql_1)
    results1 = cursor1.fetchall()
    # print (results1)
    # print (results1)
    for row in results1:
        print (row[0],row[5])
        row1=row[4]
        print ('--------')
        if results1.index(row)%2==1:
            print (row[0],row[5])
            row2=row[3]
            # print('--------***********')
            print (row1,row2)
            print('--------***********')

            if int(row1)==int(row2):
                print('ok')
            else:
                f=open("log333.txt",'a')
                f.write(row+'\n'+'两天对不上')
                f.close()
                print(row)
            print ("*"*20)


