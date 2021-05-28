from task_11_morf import Corpus
import unittest


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.corpus = Corpus()
        self.corpus.load('annot.opcorpora.no_ambig.xml')

    def test_sentence(self):
        self.assertMultiLineEqual(self.corpus.get_sentence(2), 'Великолепная «Школа злословия» вернулась в эфир после'
                                                                 ' летних каникул в новом формате.')

    def test_word(self):
        self.assertMultiLineEqual(self.corpus.get_word(2, 0), 'великолепная')

    def test_grammem(self):
        self.assertMultiLineEqual(self.corpus.get_grammem(2, 0, 0), 'ADJF')


if __name__ == '__main__':
    unittest.main()
