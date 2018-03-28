import requests
session=requests.Session()
import json
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
headers1={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Content-Type':'application/json;charset=UTF-8'}
login_url='http://192.168.1.101:52400/user/login'
data={"username":"12345678910","password":"123456"}
reponse=session.post(url=login_url,data=data,headers=headers)
maoli_url='http://192.168.1.101:52400/api/report/profit/order/list'
maoli_data={
	"limit": 222,
	"offset": 0,
	"cityIds": [320100, 320200, 320700, 321200, 320300],
	"warehouseIds": [13, 15, 4, 16, 17, 18, 113, 80, 81, 10, 7],
	"arrivedStartTime": "2018-01-01 00:00:00",
	"arrivedEndTime": "2018-03-21 23:59:59"
    }
maoli_reponse=session.post(url=maoli_url,data=json.dumps(maoli_data),headers=headers1)
data=json.loads(maoli_reponse.text)
# print (json.dumps(data, sort_keys=True, indent=2,ensure_ascii=False))
T_data=data['data']['rows']
for row in T_data:
    print(row['createdTime'])
    maoliqushui = row['profitRate']
    maolihanshui = row['profitRateWithTax']
    if maolihanshui!=None and maoliqushui!=None and round(maolihanshui,2)==round(maoliqushui,2):
       print(str(maolihanshui),str(maoliqushui)+':'+'ok')
    else:
       f = open("maoli.txt", 'a')
       f.write('毛利时间:' + row['createdTime']+'仓库:'+str(row['warehouseName'])+'订单号:'+str(row['storeGoodsOrderId'])+'\n')
       f.close()
       print(row['createdTime'], row['storeGoodsOrderId'])
    print ("*"*20)