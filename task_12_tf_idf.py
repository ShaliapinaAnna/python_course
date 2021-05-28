import xml.etree.ElementTree as etree
import json
from math import log
from collections import Counter


class tf_idf:
    def __init__(self):
        tree = etree.parse('annot.opcorpora.no_ambig.xml')
        root = tree.getroot()
        with open('task_12_idf.json', 'w', encoding='utf-8') as f:
            wordsdict = {}  # словарь для хранения слов и количества текстов, в которых они встречаются
            texts = 0  # количество текстов
            for text in root.iter('text'):
                texts += 1
                words = []
                for source in text.iter('source'):
                    source_words = source.text.split()
                    for word in source_words:
                        w1 = word.lower().rstrip('.,?!:;"\'»)').lstrip('.,?!:;"\'«(')
                        if w1 not in words:
                            words.append(w1)
                            if w1 in wordsdict.keys():
                                wordsdict[w1] += 1
                            else:
                                wordsdict[w1] = 1
            wordsdict1 = Counter(wordsdict)
            self._idf = {}
            for w in wordsdict1:
                self._idf[w] = log(texts/wordsdict[w])
            json.dump(self._idf, f, indent=4, ensure_ascii=False)

    def get_tf_idf(self, text: str):
        tf_idf = {}
        words = text.split()
        for i in range(len(words)):
            words[i] = words[i].lower().rstrip('.,?!:;"\'»)').lstrip('.,?!:;"\'«(')
        uniqwords = list(set(words))
        for word in uniqwords:
            try:
                tf = words.count(word) / len(words)
                tf_idf[word] = tf * self._idf[word]
            except KeyError:
                tf_idf[word] = 0
        return sorted(tf_idf.items(), key=lambda x: x[1])


text = tf_idf()
print(text.get_tf_idf('Пробежала полоса, широка, бела. Разделила небеса с горем пополам. Заглушила голоса, замела '
                      'глаза. Утонула полоса в девичьих слезах. Я знаю, всё будет, забудьте, люди, я так больше не '
                      'могу! Подари мне первый танец, забери меня с собой. Я повсюду иностранец и повсюду я вроде бы '
                      'свой. Словно лодка в океане затерялся берег мой... Я повсюду иностранец, забери меня, мама, '
                      'домой!'))
print(text.get_tf_idf('Больная не отвечала, но была взволнована до слёз.'))