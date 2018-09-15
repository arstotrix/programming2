import re

splitword = "s i m i l a r"
hidden_word = "s _ _ _ _ _ r"
lt = ''
hw = list(hidden_word)

while lt!= '\n':
    lt = input('input: ')
    for i,s in enumerate(splitword):
        if lt == s:
            for j,h, in enumerate(hidden_word):
                if i == j:
                    hidden_word = ''
                    hw[j] = lt
                    for q in hw:
                        hidden_word += q
    print(hidden_word)
            
