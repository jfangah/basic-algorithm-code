# %%  直接访问
   
import requests

url="http://www.baidu.com"
r=requests.get(url)
print(r.status_code)
print(r.text)

# %% 带参数访问

import requests

params={'firstname':'Ryan','lastname':'Mitchell'}

url="http://pythonscraping.com/files/processing.php"
r=requests.post(url,data=params)
print(r.status_code)
print(r.text)





# %%  爬虫伪装浏览器
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:42:07 2017

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests

url = "http://www.packtpub.com/all"
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/32.0.1667.0 Safari/537.36"}
#page = requests.get(url)
page = requests.get(url,headers=header)
soup_packtpage = BeautifulSoup(page.text,"lxml")



books =soup_packtpage.find_all('div',attrs={"class":"book-block"})

for book in books:
   booktitle =book.find('div',attrs={"class":"book-block-title"})
   bookprice =book.find('div',attrs={"class":"book-block-price"})
  
   print(booktitle.string.strip(),bookprice.get_text().strip())
   
# %%
   
#e23.1CrawUnivRanking.py
import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
def printUnivList(num):
    print("{:^4}{:^10}{:^5}{:^8}{:^10}".format("排名","学校名称","省市","总分","培养规模"))
    for i in range(num):
        u=allUniv[i]
        print("{:^4}{:^10}{:^5}{:^8}{:^10}".format(u[0],u[1],u[2],u[3],u[6]))
def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(10)
main()

# %%

#e21.1AutoKeywordSearch.py
import requests
from bs4 import BeautifulSoup
import re
import json
def getKeywordResult(keyword):
    url = 'http://www.baidu.com/s?wd='+keyword
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def parserLinks(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for div in soup.find_all('div', {'data-tools': re.compile('title')}):
        data = div.attrs['data-tools']  #获得属性值
        d = json.loads(data)        #将属性值转换成字典
        links.append(d['title'])    #将返回链接的题目返回
    return links
def main():
    html = getKeywordResult('Python语言程序设计基础(第2版)')
    ls = parserLinks(html)
    count = 1
    for i in ls:
        print("[{:^3}]{}".format(count, i))
        count += 1
main()

# %%   下载图片 二进制

"""Download flags of top 20 countries by population

Sequential version

Sample run::

    $ python3 flags.py
    BD BR CD CN DE EG ET FR ID IN IR JP MX NG PH PK RU TR US VN
    20 flags downloaded in 10.16s

"""
# BEGIN FLAGS_PY
import os
import time
import sys

import requests  # <1>

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'http://flupy.org/data/flags'  # <3>

DEST_DIR = '.'  # <4>


def save_flag(img, filename):  # <5>
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):  # <6>
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):  # <7>
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):  # <8>
    for cc in sorted(cc_list):  # <9>
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


def main(download_many):  # <10>
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)  # <11>
# END FLAGS_PY
    
# %%  异步下载
    
"""Download flags of top 20 countries by population

asyncio + aiottp version

Sample run::

    $ python3 flags_asyncio.py
    EG VN IN TR RU ID US DE CN MX JP BD NG ET FR BR PH PK CD IR
    20 flags downloaded in 1.07s

"""
# BEGIN FLAGS_ASYNCIO
import asyncio

import aiohttp  # <1>

from flags import BASE_URL, save_flag, show, main  # <2>


async def get_flag(cc):  # <3>
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = await aiohttp.request('GET', url)  # <4>
    image = await resp.read()  # <5>
    return image


async def download_one(cc):  # <6>
    image = await get_flag(cc)  # <7>
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()  # <8>
    to_do = [download_one(cc) for cc in sorted(cc_list)]  # <9>
    wait_coro = asyncio.wait(to_do)  # <10>
    res, _ = loop.run_until_complete(wait_coro)  # <11>
    loop.close() # <12>

    return len(res)


if __name__ == '__main__':
    main(download_many)
# END FLAGS_ASYNCIO
    
# %% json和xml格式

var country =
        {
            name: "中国",
            provinces: [
            { name: "黑龙江", citys: { city: ["哈尔滨", "大庆"]} },
            { name: "广东", citys: { city: ["广州", "深圳", "珠海"]} },
            { name: "台湾", citys: { city: ["台北", "高雄"]} },
            { name: "新疆", citys: { city: ["乌鲁木齐"]} }
            ]
        }    

<?xml version="1.0" encoding="utf-8" ?>
<country>
  <name>中国</name>
  <province>
    <name>黑龙江</name>
    <citys>
      <city>哈尔滨</city>
      <city>大庆</city>
    </citys>  　　
  </province>
  <province>
    <name>广东</name>
    <citys>
      <city>广州</city>
      <city>深圳</city>
      <city>珠海</city>
    </citys> 　　
  </province>
  <province>
    <name>台湾</name>
    <citys>
      　<city>台北</city>
      　<city>高雄</city>
    </citys>　
  </province>
  <province>
    <name>新疆</name>
    <citys>
      <city>乌鲁木齐</city>
    </citys>
  </province>
</country>