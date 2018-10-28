#Сделано с помощью кофеина и Никиты Логина
#Выбранный мной ресурс настолько ущербен, что эти идио кхм девелоперы пишут дату и автора в одну строку - но я с этим разобралась (sort of)

import os
import re
import urllib.request
import json
import time
from bs4 import BeautifulSoup

def getfiles(url):
    req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        text = response.read().decode('utf-8')
    return text
    
def findnews(code):
    articles = []
    for i in range(1,3554):
        try:
            url = 'http://korolev.news/news/?c=1&PageNo={}'.format(i)
            req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8')
            articles.append(text)
            #print(text[:500])
        except:
            continue
        time.sleep(0.05)
    with open ('articles.txt', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent = 4, ensure_ascii = False)
    return articles 

def findarticles(news):
    
    
def main():
    url = "http://korolev.news/news" 
    code = getfiles(url)
    news = findnews(code)
    articles = findarticles(news)
    

if __name__ == "__main__":
    main()
    
