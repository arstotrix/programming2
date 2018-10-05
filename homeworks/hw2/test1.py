import json
import urllib.request
token = "66bd781f892ea13d2c6a39e4c9597c698acab60d"

user = input('Введите имя пользователя: ')
url = f'https://api.github.com/users/{user}/repos?access_token={token}'
print(url)

response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')
data = json.loads(text)

print(len(data))
for i in data:
    print(i["language"], i['name']) 
