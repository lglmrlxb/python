import requests
from bs4 import BeautifulSoup


url="https://www.umei.cc/"
resp=requests.get(url)
resp.encoding="utf-8"
soup=BeautifulSoup(resp.text,"html.parser")
# print(soup)
list=soup.find_all("a")#查找所有的a标签
lists=[]
img=[]
s=''
#转为列表
for i  in list:
    s=str(i)
    lists.append(s)
def findstr(n,x,y):
    if n.find(x)>=0:
        s=n[n.find(x)+len(x):]
        if s.find(y)>=0:
            # print(s[:s.find(y)])
            return True,s[:s.find(y)]
        else:return False,""
    else:return False,""

for i in  lists:

    if i.find('img')>=0:
        b='data-original="'
        c='"'
        a,b=findstr(i, b, c)
        if a:
            # print(b)
            img.append(b)
print(img)

