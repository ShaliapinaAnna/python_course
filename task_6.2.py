import collections
import json
chs = collections.defaultdict(list)
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file1:
    read_file = json.load(file1)
for act in read_file['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            chs[action['character']].append(action['says'])


with open('task_62.txt', 'w', encoding='utf-8') as text:
    for character in chs:
        text.write(character + str(chs[character]) + '\n')

