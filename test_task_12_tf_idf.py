import unittest
from math import log
from task_12_tf_idf import tf_idf
from collections import Counter


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.tf_idf = tf_idf()

    def test_equal(self):
        text = 'Больная не отвечала, но была взволнована до слёз.'.lower().rstrip('.,?!:;"\'»)').lstrip('.,?!:;"\'«(')
        words = text.split(' ')
        wordsdict = Counter(words)
        for w in words:
            idf_count = log(1 / wordsdict[w])
            tf_idf_count = self.tf_idf.get_tf_idf(text)
            self.assertNotEqual(idf_count, tf_idf_count)


if __name__ == '__main__':
    unittest.main()
