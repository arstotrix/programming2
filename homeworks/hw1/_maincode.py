import random
import re

def choose_word(a):
    a = str(a)
    a += ".txt"
    with open (a, encoding = 'utf-8') as f:
        text = f.read()
        listt = text.split('\n')
    return random.choice(listt)
        
    
def encrypt_word(a):
    a = a.replace(a[1:(len(a)-1)], ' _ '*(len(a)-2))
    return a

#def playgame(a):
#def sentence(a):


a = ""
print('Давайте сыграем в виселицу!\n')
while a != "0":
    a = input('Нажмите 1, если хотите выбрать тему "Хищные птицы".\nНажмите 2, если хотите выбрать тему "Волейбол".\nНажмите 3, если хотите выбрать тему "Кофе и чай".\nНажмите 0, если вы не хотите играть.\n')
    if a not in ["0","1","2","3"]:
        print ('Извините, такой команды я не знаю.')
    if a == "0":
        print('Ладно, в другой раз.')
    else:
        print('Тогда начнём.\nНа экране будет выводиться слово, в котором пропущены все буквы, кроме первой и последней.\nБуквы Ё, Й, Ъ учитываются.\nВам даётся 7 попыток.\nЗа каждую ошибку их становится на одну меньше.\n')
        word = choose_word(a)
        hidden_word = encrypt_word(word)
        print(hidden_word)
        
        
        a = input('Хотите сыграть ещё?\nНажмите 0, если не хотите.\nНажмите 1, если хотите.\n')
        if a == "0":
            print('Спасибо за игру, до свидания!')
        elif a == "1":
            print('Отлично, погнали!')
        else:
            print('Хм, вообще-то, я говорила про единицу, но ладно, будем считать, что вы хотите играть!')
