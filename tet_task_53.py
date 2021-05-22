import unittest
import os
import shutil


def newfile(direction):
    os.makedirs('C:/Users/111/Desktop/for_test/newfile.txt')
    with open(direction, 'w') as file:
        file.write("И пусть в моих поступках не было логики, Я не умею жить по-другому")


class TestTask53(unittest.TestCase):
    def test_setUp(self):
        newfile('C:/Users/111/Desktop/for_test/newfile.txt')

    def test_empty(self):
        self.assertIsNone(os.stat('C:/Users/111/Desktop/for_test/newfile.txt').st_size == 0)

    def test_tearDown(self):
        shutil.rmtree('C:/Users/111/Desktop/for_test/newfile.txt')


if __name__ == '__main__':
    unittest.main()
