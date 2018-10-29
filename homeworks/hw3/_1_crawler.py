#Сделано с помощью кофеина и Никиты Логина
#Выбранный мной ресурс настолько ущербен, что эти идио кхм девелоперы пишут дату и автора в одну строку - но я с этим разобралась (sort of)

#import os
import re
import urllib.request
import json
import time
from bs4 import BeautifulSoup

#def getfiles(url):
#    req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
#    with urllib.request.urlopen(req) as response:
#        text = response.read().decode('utf-8')
#    return text
    
def findnews():
    articles = {}
    for i in range(1,3554):
        try:
            url = 'http://korolev.news/news/?c=1&PageNo={}'.format(i)
            req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8')
            articles[i] = text 
            print(i)
        except:
            continue
        time.sleep(0.001)
    with open ('articles_not.txt', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent = 4, ensure_ascii = False)
    #return articles 

#def findarticles(news):
#    article_data = []
#    with open ("articles.txt", 'r', encoding = 'utf-8') as f:
#        articles = json.load(f, ensure_ascii = False)
#    for a in articles:
#        soup = bs4.BeautifulSoup(a)
#        article_text = soup.find('td', {'class': "center-content"})
#        article_date = article_text.find("span", {"class": "news-date"}).get_text()
#        article_heading = article_text.find("h1").get_text()
#        article_article = article_text.find("div", {"class":"news-content"}).get_text()
#        article_text = re.sub("<.*?>","",article_text)
#        article_date = re.sub("<.*?>","",article_date)
#        article_heading = re.sub("<.*?>","",article_heading)
#        article_article = re.sub("<.*?>","",article_article)
        
    return article_data

def main():
    url = "http://korolev.news/news" 
    #code = getfiles(url)
    findnews()
    #articles = findarticles(news)
    

if __name__ == "__main__":
    main()
    
