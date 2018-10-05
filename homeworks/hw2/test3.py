import json
import urllib.request
token = "66bd781f892ea13d2c6a39e4c9597c698acab60d"
users = ['morgan1189', 'elmiram', 'nevmenandr']
leader = ''
number = 0
for user in users:
    url = "https://api.github.com/users/%s/followers?access_token=%s" % (user,token)
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    data = json.loads(text)
    if len(data) > number:
        number = len(data)
        leader = user
print(leader)    

