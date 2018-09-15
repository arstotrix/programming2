import re

def dictionarize(word):
    count = {}
    for w in word:
        if w in count:
            count[w] += 1            
        else:
            count[w] = 1       
    return count

def playgame(word, hidden_word, count):
    splitword = word[0]
    win = -1
    #rt = 0
    wrong = ''
    used = ''
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    #letters = 'abcdefghijklmnopqrstuvwxyz'
    hw = list(hidden_word)
    
    with open ('hangdude.txt', encoding = "utf-8") as f:
        text = f.read()
        pics = text.split('\n\n')
        #print(pics[0])
        
    for w in word[1:]:
        splitword = splitword + ' ' + w

    while win == -1:
        lt = input("Введите букву: ").lower()
        if lt not in letters:
            print("Что за фигню Вы только что ввели?! Я же просила буквы!")
        else:
            if lt in used:
                print("Вы уже использовали эту букву. Попробуйте ещё раз.")
            else:
                used = used + lt
                if lt in count:
                    print('Поздравляю, такая буква есть!')
                    #rt+=int(count[lt])
                    #print(rt)
                    #print(splitword)
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

win = playgame('pretender','p _ _ _ _ _ _ _ r', dictionarize('pretender'))
if win == 0:
    print('loser')
if win == 1:
    print("winner")
