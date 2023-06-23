import requests
from bs4 import BeautifulSoup
import json
import random
import time
# list_magaz=['https://www.atbmarket.com/sch?page=1&lang=uk&location=1154&query=',"https://auchan.ua/ua/catalogsearch/result/?q=","https://shop.silpo.ua/search/all?find="]

header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
src=requests.get("https://www.otomoto.pl/promoted",headers=header)
with open ('date_car/ind.html','w', encoding="utf-8") as w:
    w.write(src.text)

with open('date_car/ind.html',encoding="utf8") as file:
    src=file.read()

soup=BeautifulSoup(src,'lxml')
cars=soup.find_all("article","item")
l=[]
for i in cars:
    price=i.find("div",'hidden-mobile ooa-3ivlki').find('span')
    car=i.find('p',"ooa-8vwwc4").find('a')
    l.append(f'{car.text} --- {price.text}')

time.sleep(random.randrange(2,4))

with open('date_car/json_data.json','a',encoding="utf-8") as file:
    json.dump(l,file,indent=4,ensure_ascii=False)

for i in range(2,39):
    src=requests.get(f"https://www.otomoto.pl/promoted?page={i}",headers=header)
    with open (f'date_car/{i}.html','w', encoding="utf-8") as w:
        w.write(src.text)

    with open(f'date_car/{i}.html',encoding="utf8") as file:
        src=file.read()

    soup=BeautifulSoup(src,'lxml')
    cars=soup.find_all("article","item")
    l=[]
    for i in cars:
        price=i.find("div",'hidden-mobile ooa-3ivlki').find('span')
        car=i.find('p',"ooa-8vwwc4").find('a')
        l.append(f'{car.text} --- {price.text}')
    with open('date_car/json_data.json','a',encoding="utf-8") as file:
        json.dump(l,file,indent=4,ensure_ascii=False)
    time.sleep(random.randrange(2,4))



