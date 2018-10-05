import json
import urllib.request

datadict = {}
users = []
token = "66bd781f892ea13d2c6a39e4c9597c698acab60d"

user = input('Вводите имена пользователей гитхаба по одному. Когда закончите, нажмите Enter.\n')
while user != '':
    try:
        url = 'https://api.github.com/users/%s/repos?access_token=%s' % (user, token)
        response = urllib.request.urlopen(url)
        text = response.read().decode('utf-8')
        data = json.loads(text)
        datadict[user] = data
        users.append(user)
    except urllib.error.HTTPError:
        print('Такого пользователя нет на Гитхабе. Плиз трай эген.')
    user = input()
print(users)
#print(datadict[users[0]])
