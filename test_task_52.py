import unittest
import numpy as np


class TestTask52(unittest.TestCase):
    def test_for_nmbrs(self):
        nmbrs = np.random.random(10)
        for nmbr in nmbrs:
            with self.subTest(i=nmbr):
                self.assertGreaterEqual(nmbr, 0.5)


if __name__ == '__main__':
    unittest.main()