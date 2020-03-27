import json

u0 = dict()
u1 = dict()
u2 = dict()
data = dict()
with open('processed.json','r+',encoding="utf-8") as f:
    data = json.load(fp=f)
u0 = data['school']
u1 = data['president']
u2 = data['secret_agent']
data0 = data['inturls']

p3 = []
p2 = []
p1 = []
for url in data0:
    turl = url[0]
    score = 0
    if len(turl)>0 and turl.startswith('/'):
        turl='https://en.wikipedia.org'+url[0]
    tdat =  {"name" : url[1], "url" : turl}
    if tdat in u0:
        score += 1
    if tdat in u1:
        score += 1
    if tdat in u2:
        score += 1
    if score==3:
        p3.append(tdat)
    if score==2:
        p2.append(tdat)
    if score==1:
        p1.append(tdat)
data['p3'] = p3
data['p2'] = p2
data['p1'] = p1
with open('processed.json','r+',encoding="utf-8") as f:
    json.dump(fp=f,obj=data)