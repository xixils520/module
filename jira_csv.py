# encoding=utf-8
from prettytable import PrettyTable
from jira.client import JIRA
jira=JIRA("http://jira.diandainfo.cn:9090",basic_auth=('lisong', '123456'))
#打印登录名称
print (jira.user(jira.current_user()))
x = PrettyTable(["项目", "缺陷数量"])
x.align["name"] = "l"
x.align["name"] = "l"
#统计jira项目bug数量
for j in jira.projects():
    issues = jira.search_issues(jql_str='project=%s'%j, maxResults=100000)
    alist = []
    for u in issues:
        alist.append(u)
        i=0
        for a in alist:
            i=i+1
    x.add_row([j.name,i])
    print(x)
    # print(j.name+'缺陷数量是:',i)
# 每个项目中bug状态数量
for j in jira.projects():
    issues = jira.search_issues(jql_str='project=%s'%j, maxResults=100000)
    alist = []
    blist=[]

    for u in issues:
        alist.append(u)
    # print(alist)
    for b in alist:
        c=b.key
        # print(c)
        issue = jira.issue('%s'%c)
        if str(issue.fields.issuetype)=='故障':
            blist.append(issue)
        else:
            continue
    # print(blist)
    # print(blist)
    # print(blist)
    db = 0
    kf = 0
    cxdk = 0
    yjj = 0
    yyz = 0
    gq = 0
    byjj = 0
    xy = 0
    wc = 0
    for issue in blist:
        if str(issue.fields.status) == '完成':
        # print(str(issue.fields.status)+'wc')
            wc = wc + 1
        elif str(issue.fields.status) == '开放':
        # print(str(issue.fields.status) + 'kf')
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
        # print(str(issue.fields.status) + 'else')
            xy = xy + 1
        # print(j.name,wc,kf,cxdk,yjj,yyz,gq,byjj,xy,db)
    print(j.name+'完成状态bug数量：',wc)
    print(j.name+'开放状态bug数量：',kf)
    print(j.name+'重新打开状态bug数量：',cxdk)
    print(j.name+'已解决状态bug数量：',yjj)
    print(j.name+'已验证状态bug数量：',yyz)
    print(j.name+'挂起状态bug数量：',gq)
    print(j.name+'不予解决状态bug数量：',byjj)
    print(j.name+'响应bug状态bug数量：',xy)













