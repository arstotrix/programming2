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
    urls = {}
    for i in range(1,3554):
        try:
            url = 'http://korolev.news/news/?c=1&PageNo={}'.format(i)
            req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8')
            articles[i] = text
            urls[i] = url
            print(i)
        except:
            continue
        time.sleep(0.001)
    with open ('articles_not.txt', 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent = 4, ensure_ascii = False)
    #return articles 
    
import os
#import requests
import re
import urllib.request
import json
import time
from bs4 import BeautifulSoup

def findarticles():
    article_data = []
    with open ("articles.txt", 'r', encoding = 'utf-8') as f:
        articles = json.load(f)
    for key, a in articles.items():
        try:
            print(key)
            soup = BeautifulSoup(a, 'html.parser')
            article_text = soup.find('td', {'class': "center-content"})
            article_date = article_text.find("span", {"class": "news-date"}).get_text()
            article_heading = article_text.find("h1").get_text()
            article_article = article_text.find("div", {"class":"news-content"}).get_text()
        
            article_text = re.sub("<.*?>","",article_text)
            article_date = re.sub("<.*?>","",article_date)
            article_heading = re.sub("<.*?>","",article_heading)
            article_article = re.sub("<.*?>","",article_article)

            article_text = html.unescape(article_text)
            article_date = html.unescape(article_date)
            article_heading = html.unescape(article_heading)
            article_article = html.unescape(article_article)

            print(article_heading, article_article, article_date)
            article_data.append({'heading':article_heading, 'date': article_date, "article": article_article, 'id': key})
        except Exception:
            continue
            #print(a)
    return article_data
    
def plaintxt(data):
    month_map = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6, "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
    for article in data:
        clear_date = re_date.search(article["date"])
        day = clear_date.group(1)
        month = month_map[clear_date.group(2)]
        year = clear_date.group(3)
        path = os.path.join(".", "газета", "plain", year, month)
        escaped_name = html.escape(article["heading"]) + ".txt"
        with open(os.path.join(path, escaped_name), 'w', encoding = 'utf-8') as f:
            f.write(article["text"])

def make_dirs():
    base_path = ".\газета"
    os.makedirs(os.path.join(base_path, "plain"))
    os.makedirs(os.path.join(base_path, "mystem-xml"))
    os.makedirs(os.path.join(base_path, "mystem-plain"))
    for subfolder in ("plain", "mystem-xml", "mystem-plain"):
        for year in range(2010, 2018):
            for month in range(1, 13):
                os.makedirs(os.path.join(base_path, subfolder,
                         str(year), str(month)))

def metadata(articles_data):
    row = '%s\t-\t%s\t%s\tпублицистика\tнейтральный\tн-возраст\tн-уровень\tгородская\t%s\tВечерний Королёв\t%s\tгазета\tРоссия\tМО\tru'
    with open ('rows.csv', 'w', encoding = 'utf-8') as f:
        csv_fields = ['path', 'author', 'header', 'created', 'sphere', 'topic', 'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publ_year', 'medium', 'country', 'region', 'language']
        f.write('\t'.join(csv_fields))
        for article in articles_data:
            f.write(row %("газета/plain/"+html.escape(article['heading']), article['heading'], day+'.'+month+'.'+year, ))
            
        
        


def main():
    url = "http://korolev.news/news" 
    #code = getfiles(url)
    findnews()
    findar = findarticles()
    plaintxt(findar)
    make_dirs()
    metadata(findar)
if __name__ == "__main__":
    main()
