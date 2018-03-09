# encoding=utf-8
from jira.client import JIRA
jira=JIRA("http://jira.diandainfo.cn:9090",basic_auth=('lisong', '123456'))
#打印登录名称
print (jira.user(jira.current_user()))
# jira_test=jira.issue('CAIWU-533')
# print(jira_test.fields.assignee)
# print(jira_test.fields.reporter)

totlels=0
totlecyp=0
for j in jira.projects():
    issues = jira.search_issues(jql_str='project=%s'%j, maxResults=100000)
    i=0
    a=0

    for u in issues:
        if str(u.fields.reporter)=='李松':
            i=i+1
        if str(u.fields.reporter) == '陈玉萍':
            a = a + 1
    totlels=totlels+i
    totlecyp=totlecyp+a
    print(j.name+'缺陷数量：',i,a)
print(totlels,totlecyp)
