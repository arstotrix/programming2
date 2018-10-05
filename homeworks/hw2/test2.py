import json
import urllib.request

datadict = {}
token = "66bd781f892ea13d2c6a39e4c9597c698acab60d"
user = 'xxwlast'
url = 'https://api.github.com/users/%s/repos?access_token=%s' % (user, token)

response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')
data = json.loads(text)
for i in data:
    if i["language"] in datadict:
        datadict[i["language"]] += 1
    else:
        datadict[i["language"]] = 1
for i in datadict:
    print('Язык {} является основным в {} репозиториях'.format(i,datadict[i]))
#print(datadict)
