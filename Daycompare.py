import requests
session=requests.Session()
import json
import pymysql
db = pymysql.connect(host='192.168.1.101', port=3306, user='dddev', passwd='123456', db='ctcdb_new_test',
                     charset='utf8')
good_sql='SELECT DISTINCT(irfsds_good_id) FROM `io_report_finance_sku_daily_statistic` where irfsds_warehouse_id=53'
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
day_url='http://192.168.1.101:52400/api/report/goods/dayList'
for goodid in list:
    day_data={
        "limit": 75,
        "offset": 0,
        "cityIds": [320100],
        "warehouseIds": [53],
        "goodIds": [str(goodid)],
        "startDate": "2018-01-01 00:00:00",
        "endDate": "2018-03-21 23:59:59"
    }
    day_reponse=session.post(url=day_url,data=json.dumps(day_data),headers=headers1)
    data=json.loads(day_reponse.text)
    # print (json.dumps(data, sort_keys=True, indent=2,ensure_ascii=False))
    T_data=data['data']['rows']
    for row in T_data[:-1]:
        # print(row)
        print(row['date'])
        endnum=row['endNum']
        startnum=T_data[T_data.index(row)+1]['startNum']
        print (endnum,startnum)
        if endnum==startnum:
            print('ok')
        else:
            f=open("log111.txt",'a')
            f.write(row['date']+':'+str(row['goodId'])+'\n')
            f.close()
            print(row['date'],row['goodId'])
        print ("*"*20)