from garser.parser import Parser
from garser.element import Element
import requests
import json
# HELPING JT FIND HIS LOVE

def getData(element = Element('tag',[])):
    data = element.bodyData
    for child in element.children:
        data += getData(child)
    return data

def getLinks(element):
    link = ''
    elemnt = None
    for elem in element.getElementsByTag('a'):
        elemnt = elem
        link = elemnt.attributes.get("href")
        break
    return link

def getChildrenWithAttribute(element, attributes):
    outs = []
    for child in element.children:
        tmp = getChildrenWithAttribute(child,attributes)
        if element.attributes.get(attributes[0])==attributes[1]:
            outs.append(child)
        outs.extend(tmp)
    return outs

req = requests.get('https://en.wikipedia.org/wiki/List_of_programs_broadcast_by_Animax').text
parser = Parser()
parser.feed(req)
parser.processElements()
urls = []
element = parser.getParentElement()
children = getChildrenWithAttribute(element,['class',"div-col columns column-width"])
for child in children:
    elem = child.getElementsByTag('i')
    for elm in elem:
        urls.append((getLinks(elm),getData(elm)))
print(len(urls))
with open('test.json','w+', encoding="utf-8") as f:
    js=element.getData()
    json.dump(fp=f,obj=js)
nsurls = []
npurls = []
naurls = []
i=0
for url in urls:
    print(i+1,end="\r")
    if len(url[0])>0 and url[0].startswith('/'):
        turl = 'https://en.wikipedia.org'+url[0]
        ttxt = requests.get(turl).text
        if 'school' in ttxt.lower():
            nsurls.append({"name":url[1],"url" : turl})
        if 'president' in ttxt.lower():
            npurls.append({"name":url[1],"url" : turl})
        if 'agent' in ttxt.lower() or 'secret' in ttxt.lower():
            naurls.append({"name":url[1],"url" : turl})
    with open('processed.json','w+',encoding="utf-8") as f:
        d = dict()
        d.update({"inturls" : urls})
        d.update({"president" : npurls})
        d.update({"secret_agent" : naurls})
        d.update({"school" : nsurls})
        json.dump(fp=f,obj=d)
    i+=1