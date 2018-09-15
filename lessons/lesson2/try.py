import math
import pprint

print('5.1')
cons = 'ptk'
vow = 'ao'
for c in cons:
    for v in vow:
        print(c+v)
print('5.2')
nouns = 'cat hat'
verbs = 'shows throws'
for s in nouns.split():
    for v in verbs.split():
        for o in nouns.split():
            print(s+' '+v+' '+o)
print('1')
def mean(vals):
    return float(sum(vals)/len(vals))
print(mean([4, 5.5, 7, 5.5]))
            
#print('2')

