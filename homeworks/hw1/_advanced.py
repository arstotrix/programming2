import random
import re
import os

#функция открывает файл и случайно выбриает слово из списка
def choose_word(a):
    a = str(a)
    a += ".txt"
    with open (a, encoding = 'utf-8') as f:
        text = f.read()
        listt = text.split('\n')
    return random.choice(listt)
        
#функция зашифровывает слово для виселицы   
def encrypt_word(a):
    a = a.replace(a[1:(len(a)-1)], ' _ '*(len(a)-2))
    a = a.replace('  ',' ')
    return a
#функция разбивает слово пробелами
def splitt(word):
    splitword = word[0]
    for w in word[1:]:
        splitword = splitword + ' ' + w
    return splitword   
#функция играет с тобой в виселицу
def playgame(word, hidden_word):
    win = -1
    wrong = ''
    used = ''
    letters = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    hw = list(hidden_word)
    
    with open ('hangdude.txt', encoding = "utf-8") as f:
        text = f.read()
        pics = text.split('\n\n')
        
    splitword = splitt(word)
    
    while win == -1:
        lt = input("Введите букву: ").lower()
        if lt not in letters:
            print("Что Вы только что ввели?! Я же просила буквы!")
        else:
            if lt in used:
                print("Вы уже использовали эту букву. Попробуйте ещё раз. Но желательно другую.")
            else:
                used = used + lt
                if lt in word:
                    print('Поздравляю, такая буква есть!')
                    for i,s in enumerate(splitword):
                        if lt == s:
                            for j,h, in enumerate(hidden_word):
                                if i == j:
                                    hidden_word = ''
                                    hw[j] = lt
                                    for q in hw:
                                        hidden_word += q
                    print(hidden_word)
                else:
                    print(pics[len(wrong)])
                    wrong = wrong + lt
                    if len(wrong) == 7:
                        win = 0
                    elif len(wrong) == 6:
                        print("Осталась одна попытка!")
                    elif len(wrong) < 3:
                        print("Осталось",7-len(wrong),"попыток!")
                    else:
                        print("Осталось",7-len(wrong),"попытки!")
                    print(hidden_word)
                print("Неправильные буквы:", wrong)
                print("Использованные буквы:", used)
                
        if "_" not in hidden_word:
            win = 1
    return win
#функция записывает рекорды в файл
#def records(name, wins, fails)

#интерфейс
def main():
    a = ""
    print('Давайте сыграем в виселицу!\n')
    name = input ("Представтесь, пожалуйста, или нажмите 0, чтобы играть анонимно.\n")
    while a != "0":
        print('Нажмите 1, если хотите выбрать тему "Хищные птицы".')
        print('Нажмите 2, если хотите выбрать тему "Волейбол".')
        print('Нажмите 3, если хотите выбрать тему "Кофе и чай".')
        print('Нажмите 0, если вы не хотите играть.')
        a = input('\n')
        if a == "0":
            print('Ладно, в другой раз.')
        else:
            if a not in ["0","1","2","3"]:
                print ('Извините, такой команды я не знаю. Давайте я тогда выберу за вас.')
                a = random.randint(1,3)
                print("Ваша тема под номером",a)
            print('На экране будет выводиться слово, в котором пропущены все буквы, кроме первой и последней.')
            print('Буквы Ё, Й, Ъ учитываются.')
            print('Вам даётся 7 попыток. За каждую ошибку их становится на одну меньше.')
            print('Если буква стоит в началe или конце, это не значит, что её нет в остальном слове.')
            word = choose_word(a)
            hidden_word = encrypt_word(word)
            print("У вас есть 7 попыток, чтобы угадать слово длиной",len(word),"букв.")
            print(hidden_word)
            win = playgame(word, hidden_word)
            if win == 0:
                print("К сожалению, Вы проиграли. Загаданное слово было",word)
            elif win == 1:
                print("Поздравляю, вы отгадали слово",word)

            a = input('Хотите сыграть ещё?\nНажмите 0, если не хотите.\nНажмите 1, если хотите.\n')
            if a == "0":
                print('Спасибо за игру, до свидания!')
            elif a == "1":
                print('Отлично, погнали!')
            else:
                print('Хм, вообще-то, я говорила про единицу, но ладно, будем считать, что вы хотите играть!')

if __name__ == "__main__":
    main()
