import json
import requests
import pymysql
session=requests.Session()
db = pymysql.connect(host='192.168.1.101', port=3306, user='dddev', passwd='123456', db='ctcdb_new_test',
                     charset='utf8')
good_sql='SELECT DISTINCT(irfsds_good_id) FROM `io_report_finance_sku_daily_statistic` where irfsds_warehouse_id=7'
cursor=db.cursor()
cursor.execute(good_sql)
results=cursor.fetchall()
list=[]
for row in results:
    row=row[0]
    list.append(row)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
headers1={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Content-Type':'application/json;charset=UTF-8'}
login_url='http://192.168.1.101:52400/user/login'
data={"username":"12345678910","password":"123456"}
reponse=session.post(url=login_url,data=data,headers=headers)
day_url='http://192.168.1.101:52400/api/report/goods/list/detail'
for goodid in list:
    print(goodid)
    day_data={
	"offset": 0,
	"cityIds": [320300],
	"warehouseIds": [7],
	"goodIds": [goodid],
	"firstCatalogId": "果蔬汁",
	"secondCatalogId": "饮料",
	"goodsBrandName": "可口可乐",
	"goodsName": "美汁源果粒橙  1.25L*12瓶/箱",
	"startTime": "2010-01-01 00:00:00",
	"endTime": "2018-03-22 15:40:34"
    }
    day_reponse=session.post(url=day_url,data=json.dumps(day_data),headers=headers1)
    data=json.loads(day_reponse.text)
    # print (json.dumps(data, sort_keys=True, indent=2,ensure_ascii=False))
    print(data)
    if data['status']==1:
        T_data=data['data']['rows']
        for row in T_data[:-1]:
            # print(row)
            print(row['time'])
            endnum=row['endNum']
            startnum=T_data[T_data.index(row)+1]['startNum']
            print (endnum,startnum)
            if endnum==startnum:
                print('ok')
            else:
                f=open("log222.txt",'a')
                f.write(row['time']+':'+str(goodid)+'\n')
                f.close()
                print(row['time'],str(goodid))
            print ("*"*20)