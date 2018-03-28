# coding=utf-8
import requests
import json
session=requests.Session()
import pymysql
db = pymysql.connect(host='192.168.1.101', port=3306, user='dddev', passwd='123456', db='ctcdb_new_test',
                     charset='utf8')
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
login_url='http://192.168.1.251:30011/login'
userphone=input('请输入登录账号：')
login_response=session.post(url=login_url,data={"auto": "true",
                                              "plugin[ih]": 246,
                                              "plugin[iw]": 1916,
                                              "plugin[sh]": 1080,
                                              "plugin[sw]": 1920,
                                              "plugin[ua]": headers,
                                              "pwd": 123456,
                                              "uid": userphone},headers=headers)
print(login_response.text)
data=json.loads(login_response.text)
print (json.dumps(data, sort_keys=True, indent=2,ensure_ascii=False))
order_url='http://192.168.1.251:30011/api/user/order/detail'
order_oid=input('请输入订单编号:')
order_data={"oid":order_oid}
order_reponse=session.post(url=order_url,data=order_data,headers=headers)
data=json.loads(order_reponse.text)
yingfu=data['order']['sum']
zengdou=data['order']['dadouOff']
manjian=data['order']['fullCutOff']
youhuiquan=data['order']['couponCodeOff']
dadou=data['order']['dadouUseOff']
hongbao=data['order']['redGiftOff']
zongjine=round(float(yingfu)+float(zengdou)+float(manjian)+float(youhuiquan)+float(dadou)+float(hongbao),2)
print(zongjine)
#计算满减商品金额
sql1 = 'SELECT SUM(`SUM`) FROM `store_goods_order_details` WHERE StoreGoodsOrderId={0} AND promotions LIKE "%fullCutId%";'.format(order_oid)
course1 = db.cursor()
course1.execute(sql1)
result1=course1.fetchone()
course1.close()
print(float(result1[0]))
#计算赠品价值
zengpinchengben=input('请输入赠品成本：')
sql2='SELECT SUM(amount) FROM `store_goods_order_details` WHERE StoreGoodsOrderId={0} AND price=0'.format(order_oid)
course2 = db.cursor()
course2.execute(sql2)
result2=course2.fetchone()
course2.close()
print(float(result2[0]))
result2=float(result2[0])
sql3='SELECT SUM(`SUM`) FROM `store_goods_order_details` WHERE StoreGoodsOrderId={0} AND promotions LIKE "%fullGiftAssignId%";'.format(order_oid)
course3 = db.cursor()
course3.execute(sql2)
result3=course3.fetchone()
course3.close()
print(float(result3[0]))
result3=float(result3[0])
OrderDetail=data['order']['orderDetails']
for row in OrderDetail:
    goodid=row['GoodId']
    price=row['price']
    amount=row['amount']
    sum=row['sum']
    dadouOff=row['dadouOff']
    onSellGoodId=row['onSellGoodId']
    sql='SELECT Promotions FROM `store_goods_order_details` WHERE StoreGoodsOrderId="%(order_oid)s" AND OnSellGoodId="%(OnSellGoodId)s";'%{'order_oid':order_oid,'OnSellGoodId':onSellGoodId}
    course=db.cursor()
    course.execute(sql)
    result =course.fetchone()
    result=json.loads(result[0])
    #打印每个sku的达豆立减金额
    print(str(goodid)+"立减达豆优惠是："+str(dadouOff))
    #第二步统计满减满赠sku
    if 'fullCutId' in result.keys():
        print(str(goodid)+"参与满减，商品金额："+str(sum))
#计算满减金额分摊
        manjianfentan=manjian*sum/float(result1[0])
        print(str(goodid)+"参与满减的分摊"+str(manjianfentan))
    else:
        print(str(goodid) + "参与满减的分摊:0")
    if 'fullGiftAssignId' in result.keys():
        print(str(goodid)+"参与满赠")
        manzengfentan=float(zengpinchengben)*(result2)/(result3)
        print(str(goodid)+"参与满赠的商品分摊"+str(manzengfentan))
    else:
        print(str(goodid) + "参与满赠的分摊:0")
    #计算每个sku的红包优惠券分摊
    erjifenmu=zongjine-zengdou
    hongbaofentan=(hongbao+youhuiquan)*(sum/erjifenmu)
    print(str(goodid)+'达豆优惠券分摊金额:'+str(hongbaofentan))
    #计算每个sku的账户达豆分摊
    fenmu=erjifenmu-hongbao-youhuiquan-manjian
    zhanghuddft=dadou*(sum-hongbaofentan)/fenmu
    print(str(goodid)+'账户达豆分摊：'+str(zhanghuddft))
    tuihuojia=sum-hongbaofentan-zhanghuddft-manjianfentan
    print(str(goodid)+'退货价格是：'+str(tuihuojia))






