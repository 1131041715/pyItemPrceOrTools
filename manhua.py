
# coding=UTF-8
import requests
from urllib import parse
from bs4 import BeautifulSoup
import threading
import os
import sys

_name=input('请输入你想看的漫画:')

try:
    os.mkdir('./{}'.format(_name))
except:
    print('已经存在相同的文件夹了,程序无法在继续进行！')
    sys.exit()

name_=parse.urlencode({'keyword':_name})
url='https://www.mkzhan.com/search/?{}'.format(name_)
html=requests.get(url=url)
content=html.text
soup=BeautifulSoup(content,'lxml')
list1=soup.select('div.common-comic-item')
names=[]
hrefs=[]
keywords=[]
for str1 in list1:
    names.append(str1.select('p.comic__title>a')[0].get_text())   # 匹配到的漫画名称
    hrefs.append(str1.select('p.comic__title>a')[0]['href'])      # 漫画的网址
    keywords.append(str1.select('p.comic-feature')[0].get_text())          # 漫画的主题
print('匹配到的结果如下：')
for i in range(len(names)):
    print('【{}】-{}     {}'.format(i+1,names[i],keywords[i]))

i=int(input('请输入你想看的漫画序号:'))
print('你选择的是{}'.format(names[i-1]))


url1='https://www.mkzhan.com'+hrefs[i-1]      # 漫画的链接
html1=requests.get(url=url1)
content1=html1.text
soup1=BeautifulSoup(content1,'lxml')
str2=soup1.select('ul.chapter__list-box.clearfix.hide')[0]
list2=str2.select('li>a')
name1=[]
href1=[]
for str3 in list2:
    href1.append(str3['data-hreflink'])   # 漫画一章的链接
    name1.append(str3.get_text().strip()) # 漫画一章的题目,去空格

def Downlad(href1,path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}
    url2='https://www.mkzhan.com'+href1
    html2=requests.get(url=url2,headers=headers)
    content2=html2.text
    soup2=BeautifulSoup(content2,'lxml')
    list_1=soup2.select('div.rd-article__pic.hide>img.lazy-read')  # 漫画一章中的所有内容列表
    urls=[]
    for str_1 in list_1:
        urls.append(str_1['data-src'])

    for i in range(len(urls)):
        url=urls[i]
        content3=requests.get(url=url,headers=headers)
        with open(file=path+'/{}.jpg'.format(i+1),mode='wb') as f:
            f.write(content3.content)
    return True


def Main_Downlad(href1:list,name1:list):
    while True:
        if len(href1)==0:
            break
        href=href1.pop()
        name=name1.pop()
        try:
            path='./{}/{}'.format(_name,name)
            os.mkdir(path=path)
            if Downlad(href, path):
                print('线程{}正在下载章节{}'.format(threading.current_thread().getName(),name))
        except:
            pass

threading_1=[]
for i in range(30):
    threading1=threading.Thread(target=Main_Downlad,args=(href1,name1,))
    threading1.start()
    threading_1.append(threading1)
for i in threading_1:
    i.join()
print('当前线程为{}'.format(threading.current_thread().getName()))
