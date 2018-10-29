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
    os.mkdir(os.path.join(base_path, "plain"))
    os.mkdir(os.path.join(base_path, "mystem-xml"))
    os.mkdir(os.path.join(base_path, "mystem-plain"))
    for subfolder in ("plain", "mystem-xml", "mystem-plain"):
        for year in range(2010, 2018):
            for month in range(1, 13):
                os.mkdir(os.path.join(base_path, subfolder,
                         str(year), str(month)))
def main():
    plaintxt(findarticles())
    make_dirs
if __name__ == "__main__":
    main()
    
