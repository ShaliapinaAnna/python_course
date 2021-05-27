import unittest
from math import log
from tfidf import TfIdf


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.text = TfIdf('task_12_tf_idf.json', 'annot.opcorpora.no_ambig.xml')

    def test_tfidf(self):
        self.assertMultiLineEqual(str(self.text.get_tf_idf('больная, иностранец')),
                                  f'[(\'иностранец\', {0}), (\'больная\', {0.5 * log(4062)})]')


if __name__ == '__main__':
    unittest.main()
