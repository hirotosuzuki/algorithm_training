import unittest
from algorithm_training.dp_matome import *
from .base import BaseInputTests

class InputTestsA_Frog1(BaseInputTests):
    task = TaskA_Frog1()

    def test_1(self):
        input_text = """4
10 30 40 20
"""
        expected = "30\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """2
10 10
"""
        expected = "0\n"
        self._run(input_text, expected, self.task)

    def test_3(self):
        input_text = """6
30 10 60 10 60 50
"""
        expected = "40\n"
        self._run(input_text, expected, self.task)

class InputTestsB_Frog2(BaseInputTests):
    task = TaskB_Frog2()

    def test_1(self):
        input_text = """5 3
10 30 40 50 20
"""
        expected = "30\n"
        self._run(input_text, expected, self.task)

    @unittest.skip("")
    def test_2(self):
        input_text = """"""
        expected = "\n"
        self._run(input_text, expected, self.task)

    @unittest.skip("")
    def test_3(self):
        input_text = """"""
        expected = "\n"
        self._run(input_text, expected, self.task)


class InputTestsC_Vacation(BaseInputTests):
    task = TaskC_Vacation()

    def test_1(self):
        input_text = """3
10 40 70
20 50 80
30 60 90
"""
        expected = "210\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """1
100 10 1
"""
        expected = "100\n"
        self._run(input_text, expected, self.task)

    def test_3(self):
        input_text = """7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1
"""
        expected = "46\n"
        self._run(input_text, expected, self.task)


# class InputTestsD(BaseInputTests):
#     task = TaskD()

#     @unittest.skip("")
#     def test_1(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)


# class InputTestsE(BaseInputTests):
#     task = TaskE()

#     @unittest.skip("")
#     def test_1(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)


# class InputTestsF(BaseInputTests):
#     task = TaskF()

#     @unittest.skip("")
#     def test_1(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)