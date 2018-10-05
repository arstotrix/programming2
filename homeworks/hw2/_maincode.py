#ПРОЧТИТЕ, ПОЖАЛУЙСТА!!!
#Токен мой. Он упомянут в retrieve() и retrievefoll() - строки 25 и 34 соответственно. Можете заменить на свой. Лучше замените на свой.  

import json
import urllib.request

#функция получает имена пользователей на гитхабе
def getusers():
    users = []
    a = input('Вводите имена пользователей гитхаба по одному. Когда закончите, нажмите Enter.\n')
    while a != '':
        users.append(a)
        a = input()
    #print(users)
    return users

#функция проверяет существование юзера
def check(username, users):
    while username not in users:
        username = input('Такого пользователя у нас нет. Попробуйте ещё раз: ')
    return username

#функция запрашивает данные о репозиториях с сервера        
def retrieve(username):
    token = "66bd781f892ea13d2c6a39e4c9597c698acab60d"
    url = 'https://api.github.com/users/%s/repos?access_token=%s' % (username, token)
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    data = json.loads(text)
    return data

#функция, специально написанная для пятой задачи (запрашивает данные о фолловерах)
def retrievefoll(username):
    token = "66bd781f892ea13d2c6a39e4c9597c698acab60d"
    url = 'https://api.github.com/users/%s/followers?access_token=%s' % (username, token)
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    data = json.loads(text)
    return data

#функция ищет репозитории пользователя
def user_repos(username, users):
    username = check(username,users)
    data = retrieve(username)
    print('Вы выбрали пользователя:',username)
    
    print("Количество репозиториев пользователя:", len(data))
    for i in data:
        print('{}: "{}".'.format(i["name"], i['description'])) 
    return 0
    
#функция определяет список языков пользователя    
def user_languages(username, users):
    datadict = {}
    #print(username)
    username = check(username,users)
    data = retrieve(username)
    print('Вы выбрали пользователя:',username)
    for i in data:
        if i["language"] in datadict:
            datadict[i["language"]] += 1
        else:
            datadict[i["language"]] = 1
    for i in datadict:
        print('Язык {} является основным в {} репозиториях'.format(i,datadict[i]))    
    return datadict

#функция определяет пользователя с наибольшим количеством репозиториев
def most_repos(users):
    leader = ''
    number = 0
    for user in users:
        data = retrieve(user)
        if len(data) > number:
            number = len(data)
            leader = user
        if len(data) == number and leader != user:
            leader = leader + ' и ' + user
    return leader

#функция определяет самый популярный язык
def most_languages(users):
    datadict = {}
    leader = ''
    number = 0
    for user in users:
        data = retrieve(user)
        for i in data:
            if i["language"] in datadict:
                datadict[i["language"]] += 1
            else:
                datadict[i["language"]] = 1
    for d in datadict:
        if datadict[d] > number:
            number = datadict[d]
            leader = d
        if datadict[d] == number and leader != d:
            leader = leader + ' и ' + d
    return 'Самый популярный язык - {}; он используется {} раз.'.format(leader, number)

#функция определяет самого популярного пользователя
def most_followers(users):
    leader = ''
    number = 0
    for user in users:
        data = retrievefoll(user)
        if len(data) > number:
            number = len(data)
            leader = user
        if len(data) == number and leader != user:
            leader = leader + ' и ' + user
    return leader

def main():
    users = getusers()  
    user_repos(input('Введите имя пользователя: '), users)
    datadict = user_languages(input('Введите имя пользователя: '), users)
    print('Больше всех репозиториев у пользователя: {}'.format(most_repos(users)))
    print(most_languages(users))
    print('Самый популярный пользователь: {}'.format(most_followers(users)))

if __name__ == '__main__':
    main()
