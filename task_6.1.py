import collections
import json
words = collections.Counter()
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file1:
    read_file = json.load(file1)
    for act in read_file['acts']:
        for scene in act['scenes']:
            for action in scene['action']:
                w = ' '.join(action['says']).replace('?', ' ').replace(',', ' ').replace('!', ' ').replace(':', '').replace('-', ' ').replace('.', ' ').replace('[', ' ').replace(']', ' ').replace("'", ' ').replace(';', ' ').replace('"', ' ').lower()
                wo = w.split(' ')
                for word in wo:
                    if word != '':
                        words[word] += 1

often_list = words.most_common(20)
rarely_list = words.most_common()[-20:-1]
print(often_list, '\n', rarely_list)
