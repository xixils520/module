from prettytable import PrettyTable
import csv
# x = PrettyTable(["name", "age", "sex", "money"])
# x.align["name"] = "l"
# x.align["name"] = "l"
# x.add_row(["wang", 20, "man", 1000])
# x.add_row(["alex",21, "man", 2000])
# print(x)


with open("test.csv","w") as csvfile:
    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
