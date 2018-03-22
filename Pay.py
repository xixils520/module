import pymysql.cursors
import time
import datetime

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=3)
start = '23:59:59'
a = str(today) + ' ' + str(start)
b = str(yesterday) + ' ' + str(start)
print(a, b)
db = pymysql.connect(host='192.168.1.101', port=3306, user='dddev', passwd='123456', db='ctcdb_new_test',
                     charset='utf8')
# sql(查询分流订单数)
amount1 = 'SELECT    COUNT(id) FROM   store_order_branches  WHERE arrivedTime > "%(b)s"  AND arrivedTime < "%(a)s"   AND CityId="320100" AND StoreGoodsOrderId IN    (SELECT      StoreGoodsOrderId    FROM     `store_goods_order_pay_type`    WHERE payType IN (2, 3)      AND state IN (10, - 99))' % {
    'a': a, 'b': b}
amount2 = ' SELECT    count(id) FROM   store_order_branches   WHERE arrivedTime > "%(b)s" AND CityId="320100"  AND arrivedTime < "%(a)s"  AND state IN (10,20)   AND payOnDeliveryState=1   AND id IN (SELECT    bcs_store_order_branch_id FROM   branch_check_sales  WHERE  bcs_check_state=99 AND bcs_pay_method IN (2,3)  )' % {
    'a': a, 'b': b}
cursor = db.cursor()
cursor.execute(amount1)
results1 = cursor.fetchone()
for num1 in results1:
    mum1 = num1
cursor.execute(amount2)
results2 = cursor.fetchone()
for num2 in results2:
    mum2 = num2
num = num1 + num2
print('分流单个数是：' + str(num))
# 查询分流单金额
sql = 'SELECT  sum(sum) FROM   store_order_branches   WHERE arrivedTime > "%(b)s"   AND arrivedTime < "%(a)s"  AND CityId="320100" AND state IN (10,20)   AND payOnDeliveryState=1   AND id IN (SELECT    bcs_store_order_branch_id FROM   branch_check_sales  WHERE  bcs_check_state=99 AND bcs_pay_method IN (2,3))' % {
    'a': a, 'b': b}
cursor.execute(sql)
results3 = cursor.fetchone()
for sum in results3:
    continue
print('分流单总金额是：' + str(sum))

