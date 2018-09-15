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
    rt = 0
    wrong = ''
    used = ''
    #letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    with open ('hangdude.txt', encoding = "utf-8") as f:
        text = f.read()
        pics = text.split('\n\n')
        #print(pics[0])
        
    for w in word[1:]:
        splitword = splitword + ' ' + w

    while win == -1:
        l = input("Введите букву: ").lower()
        if l not in letters:
            print("Что за фигню Вы только что ввели?! Я же просила буквы!")
        else:
            if l in used:
                print("Вы уже использовали эту букву. Попробуйте ещё раз.")
            else:
                used = used + l
                if l in count:
                    print('Поздравляю, такая буква есть!')
                    rt+=int(count[l])
                    print(splitword)
                    i = 0
                    for s in splitword:
                        if s == l:
                            print(hidden_word[i])
                            hidden_word = hidden_word.replace(hidden_word[i], l)
                        i += 1
                        #print(i)
                        print(hidden_word)
                else:
                    print(pics[len(wrong)])
                    wrong = wrong + l
                    if len(wrong) == 7:
                        win = 0
                    elif len(wrong) == 6:
                        print("Осталась одна попытка!")
                    elif len(wrong) < 3:
                        print("Осталось",7-len(wrong),"попыток!")
                    else:
                        print("Осталось",7-len(wrong),"попытки!")
                    print(hidden_word)
                print("Неправильные буквы: ", wrong)
                
        if rt == len(word):
            win = 1    
    return win

win = playgame('pretender','p _ _ _ _ _ _ _ r', dictionarize('pretender'))
if win == 0:
    print('loser')
if win == 1:
    print("winner")
