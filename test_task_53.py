import unittest
import os
import shutil


class TestTask53(unittest.TestCase):
    def setUp(self) -> None:
        self.path = 'C:\\Users\\HOME-PC\\PycharmProjects\\python_course\\test_task'
        os.makedirs(self.path, exist_ok=True)
        with open('C:\\Users\\HOME-PC\\PycharmProjects\\python_course\\test_task\\task53_песня.txt', 'w') as f:
            f.write('Назад от праздников ко Вторникам\nНазад от финиша к исходникам\nИ пусть в моих поступках не было логики\nЯ не умею жить по-другому')

    def test_cheking(self):
        with open('C:\\Users\\HOME-PC\\PycharmProjects\\python_course\\test_task\\task53_песня.txt', 'r') as for_checking:
            text = for_checking.read()
            self.assertTrue(text != '')
            self.assertTrue(text == 'Назад от праздников ко Вторникам\nНазад от финиша к исходникам\nИ пусть в моих поступках не было логики\nЯ не умею жить по-другому')

    def tearDown(self) -> None:
        shutil.rmtree('C:\\Users\\HOME-PC\\PycharmProjects\\python_course\\test_task')


if __name__ == '__main__':
    unittest.main()
