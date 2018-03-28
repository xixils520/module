# encoding=utf-8
from jira.client import JIRA
from pychartdir import *
jira=JIRA("http://jira.diandainfo.cn:9090",basic_auth=('lisong', '123456'))
#打印登录名称
print (jira.user(jira.current_user()))
# jira_test=jira.issue('CAIWU-533')
# print(jira_test.fields.assignee)
# print(jira_test.fields.reporter)
issues001=jira.search_issues(jql_str='issuetype = 故障 AND created >= 2018-01-01 AND created <= 2018-01-31',maxResults=500)
x=0
wancheng=0
guaqi=0
chongxindakai=0
for a in issues001:
    if str(a.fields.status) == '完成':
        wancheng=wancheng+1
    if str(a.fields.status) == '挂起':
        guaqi=guaqi+1
    if str(a.fields.status) == '重新打开':
        chongxindakai=chongxindakai+1
ylist=[wancheng,guaqi,chongxindakai]
c = XYChart(500, 500)
c.setPlotArea(50, 50, 400, 400)
xlist=['完成','已解决','重新打开']
print(xlist,ylist)
c.addBarLayer(ylist)
c.xAxis().setLabels(xlist)
c.yAxis().setLabelStyle("FZYTK.TTF", 10, 0xcc6600)
c.xAxis().setLabelStyle("FZYTK.TTF", 10, 0x008000).setFontAngle(45)
c.makeChart("jira002.png")

#
# xiangmulist=[]
# amountlist=[]
# for j in jira.projects():
#     issues = jira.search_issues(jql_str='project=%s'%j, maxResults=100000)
#     i=0
#     for bug in issues:
#         if str(bug.fields.issuetype) == '故障':
#             i=i+1
#     # print(j.name,i)
#     xiangmulist.append(j.name)
#     amountlist.append(str(i))
# print(xiangmulist,amountlist)
# c = XYChart(1000, 1000)
# c.setPlotArea(100, 100, 800, 800)
# c.addBarLayer(amountlist)
# c.xAxis().setLabels(xiangmulist)
# c.yAxis().setLabelStyle("FZYTK.TTF", 10, 0xcc6600)
# c.xAxis().setLabelStyle("FZYTK.TTF", 10, 0x008000).setFontAngle(45)
# c.makeChart("jira001.png")
#统计每个项目中李松报告的bug数量
#     for u in issues:
#         if str(u.fields.reporter)=='李松':
#             i=i+1
#         if str(u.fields.reporter) == '陈玉萍':
#             a = a + 1
# #统计报告的所有bug数量
#     totlels=totlels+i
#     totlecyp=totlecyp+a
#     print(j.name+'缺陷数量：',i,a)
#
# print(totlels,totlecyp)


# # The data for the bar chart
# data = [85, 156, 179.5, 211, 123]
#
# # The labels for the bar chart
# labels = ["Mon", "Tue", "Wed", "Thu", "Fri"]
#
# # Create a XYChart object of size 250 x 250 pixels
# c = XYChart(250, 250)
#
# # Set the plotarea at (30, 20) and of size 200 x 200 pixels
# c.setPlotArea(30, 20, 200, 200)
#
# # Add a bar chart layer using the given data
# c.addBarLayer(data)
#
# # Set the labels on the x axis.
# c.xAxis().setLabels(labels)

# Output the chart
# c.makeChart("simplebar.png")
