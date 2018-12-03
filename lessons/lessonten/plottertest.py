import matplotlib
import csv

import csv

with open('nanai-vowels.csv', encoding='utf-8') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in filereader: # row - это список
        pass # здесь то, что нужно сделать со строками таблицы
