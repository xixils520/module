import json
tuple001=('{"fullCutId":380,"onSale":0,"dadou":0,"belongsVip":0}',)
tt=json.loads(tuple001[0])
if  "fullCutId" in tt.keys():
    print('ok')

# str001="".join(tuple001)
# str002=str001.replace("{","")
# str003=str002.replace("}","")
# print(str003)
# dict001={}
# str003=str003.split(',')
# for data in str003:
#     x,y=data.split(':')
#     if y:
#         print(y)
#         dict001[x]=y
# print(dict001)
# print(dict001[])