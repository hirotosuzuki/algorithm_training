from algorithm_training.abc87 import *
from .base import BaseInputTests

class InputTestsA(BaseInputTests):
    task = TaskA()

    def test_1(self):
        input_text = """"""
        expected = "\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """"""
        expected = "\n"
        self._run(input_text, expected, self.task)

    def test_3(self):
        input_text = """"""
        expected = "\n"
        self._run(input_text, expected, self.task)

class InputTestsB(BaseInputTests):
    task = TaskB()

    def test_1(self):
        input_text = """5
1
0
150
"""
        expected = "0\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """30
40
50
6000
"""
        expected = "213\n"
        self._run(input_text, expected, self.task)

    # def test_3(self):
    #     input_text = """"""
    #     expected = "\n"
    #     self._run(input_text, expected, self.task)