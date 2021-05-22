import csv
import collections
from collections import OrderedDict
dictionary = {}
with open('stage3_test.csv', encoding='utf-8') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        dictionary[row["Title"]] = float(row["Price"])

with open('csv642.txt', 'w', encoding='utf-8') as text:
    text.write(str(OrderedDict(sorted(dictionary.items(), key=lambda t: t[1]))))
    text.write(str(OrderedDict(sorted(dictionary.items(), key=lambda t: t[1], reverse=True))))
