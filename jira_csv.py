# encoding=utf-8
from jira.client import JIRA
import csv
jira=JIRA("http://jira.diandainfo.cn:9090",basic_auth=('lisong', '123456'))
#打印登录名称
print (jira.user(jira.current_user()))
# 统计jira项目bug数量
emptyArr = []
emptyArr1 = []
for j in jira.projects():
    issues = jira.search_issues(jql_str='project=%s'%j, maxResults=100000)
    alist = []
    blist=[]

    for u in issues:
        alist.append(u)
    for b in alist:
        c=b.key
        # print(c)
        issue = jira.issue('%s'%c)
        if str(issue.fields.issuetype)=='故障':
            blist.append(issue)
        else:
            continue

    db = 0
    kf = 0
    cxdk = 0
    yjj = 0
    yyz = 0
    gq = 0
    byjj = 0
    xy = 0
    wc = 0
    print(blist)
    for issue in blist:
        if str(issue.fields.status) == '完成':
        # print(str(issue.fields.status)+'wc')
            wc = wc + 1
        elif str(issue.fields.status) == '开放':

            kf = kf + 1
        elif str(issue.fields.status) == '重新打开':
        # print(str(issue.fields.status) + 'cxdk')
            cxdk = cxdk + 1

        elif str(issue.fields.status) == '已解决':
            yjj = yjj + 1

        elif str(issue.fields.status) == '已验证':
            yyz = yyz + 1

        elif str(issue.fields.status) == '挂起':
            gq = gq + 1

        elif str(issue.fields.status) == '不予解决':
            byjj = byjj + 1

        elif str(issue.fields.status) == '待办':
            db = db + 1

        else:

            xy = xy + 1
    emptyArr1.append([j.name, '完成', wc])
    emptyArr1.append([j.name, '开放', kf])
    emptyArr1.append([j.name, '重新打开', cxdk])
    emptyArr1.append([j.name,'已解决' , yjj])
    emptyArr1.append([j.name,'已验证', yyz])
    emptyArr1.append([j.name,'挂起' , gq])
    emptyArr1.append([j.name,'不予解决' , byjj])
    emptyArr1.append([j.name,'待办' , db])
    emptyArr1.append([j.name, '响应', xy])
    print(emptyArr1)
    with open("test001.csv", "w",newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["项目名称", "缺陷状态",'缺陷数量'])
        # 写入多行用writerows
        writer.writerows(emptyArr1)
        i = 0
        for b in blist:
            i = i + 1;
        emptyArr.append([j.name, i])
    print(emptyArr)
    with open("test.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["项目名称", "缺陷数量"])
        # 写入多行用writerows
        writer.writerows(emptyArr)













