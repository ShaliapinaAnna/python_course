import collections
import json
chs = {}
with open('RomeoAndJuliet.json', 'r', encoding='utf-8') as file1:
    read_file = json.load(file1)
    for act in read_file['acts']:
        for scene in act['scenes']:
            for action in scene['action']:
                chs[action['character']] = len(action['says'])

chs2 = collections.Counter(chs)
print(chs2.most_common())
