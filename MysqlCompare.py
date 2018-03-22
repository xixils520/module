import pymysql.cursors
import datetime
import time
import os, sys
#测试环境对比月结数据。一月的期末=二月的期初。如果不等输出
db = pymysql.connect(host='192.168.1.101', port=3306, user='dddev', passwd='123456', db='ctcdb_new_test',
                     charset='utf8')
#查询仓库
good_sql='SELECT DISTINCT(irfsds_good_id) FROM `io_report_finance_sku_daily_statistic` where irfsds_warehouse_id=7'
cursor=db.cursor()
cursor.execute(good_sql)
results=cursor.fetchall()
list=[]
for row in results:
    row=row[0]
    list.append(row)
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
print('开始时间',now)
for goodid in list:
    goodid=str(goodid)
#一月月结
    January_sql='SELECT SUM(irfsds_start_num),SUM(irfsds_end_num) FROM io_report_finance_sku_daily_statistic WHERE irfsds_warehouse_id=7 AND irfsds_date="2018-01-01" AND irfsds_good_id=%s AND irfsds_type=2; '%goodid
    February_sql='SELECT SUM(irfsds_start_num),SUM(irfsds_end_num) FROM io_report_finance_sku_daily_statistic WHERE irfsds_warehouse_id=7 AND irfsds_date="2018-02-01" AND irfsds_good_id=%s AND irfsds_type=2; '%goodid
    cursor_1 = db.cursor()
    cursor_1.execute(January_sql)
    results1=cursor_1.fetchone()
    cursor_2 = db.cursor()
    cursor_2.execute(February_sql)
    results2=cursor_2.fetchone()
    if results1[1]!=None and results2[0]!=None and results1[0]!=None and results2[1]!=None and results1[1] == results2[0]:
        print('正确')
        # f=open("log.txt",'a')
        # f.write(January_sql+'正确\n')
    elif results1[1]!=None and results2[0]!=None and results1[0]!=None and results2[1]!=None and results1[1] != results2[0]:
        print('None')
        f=open("log.txt",'a')
        f.write(January_sql+'对不上\n')
        f.close()
    else:
        print('空的')
        # f=open("log.txt",'a')
        # f.write(January_sql+'空的\n')


    cursor_1.close()
    cursor_2.close()
db.close()
end = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
print('结束时间', end)








