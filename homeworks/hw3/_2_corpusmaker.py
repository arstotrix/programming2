import os
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
        soup = bs4.BeautifulSoup(a)
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
    return article_data

def main():
    articles = findarticles()
    
if __name__ == "__main__":
    main()
    
