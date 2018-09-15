import re

word = 'blessing'
splitword = word[0]
for w in word[1:]:
    splitword = splitword + '  ' + w
    #splitword.replace()
splitword = re.sub('  ',' ', splitword)
print(splitword)
