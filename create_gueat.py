# import pymysql
import pymysql.cursors
# # f=open("1122.txt",'w')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='guest', charset='utf8')
for a in range(290,200):
    str_a=str(a)
    name="发布会"+str_a
    limit=str_a
    sql='INSERT INTO guest.sign_event(`name`,`limit`,`status`,address) VALUES("'+name+'","'+limit+'",1,"地址");'
    for i in range(7180,7192):
            str_i=str(i)
            realname="jack"+str_i
            phone=13800000000+i
            email="jack"+str_i+"@email.com"
            sql1='INSERT INTO guest.sign_guest(realname,phone,email,sign,event_id) VALUES("'+realname+'",'+str(phone)+',"'+email+'",0,"'+str_a+'");'
            curseor1=db.cursor()
            curseor1.execute(sql)
            curseor1.execute(sql1)
            db.commit()
    print(str_a+"%")

db.close()

