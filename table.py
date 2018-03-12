from prettytable import PrettyTable
import csv
# x = PrettyTable(["name", "age", "sex", "money"])
# x.align["name"] = "l"
# x.align["name"] = "l"
# x.add_row(["wang", 20, "man", 1000])
# x.add_row(["alex",21, "man", 2000])
# print(x)


with open("test001.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(["项目名称","缺陷数量"])
    #写入多行用writerows
    writer.writerows([['COCACOLA',1],['test',1],['业务员系统',237],['加盟商',2],['后台',525],['商城',432],['小程序',271],['店达官网',1]])
