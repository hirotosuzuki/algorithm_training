import unittest
from algorithm_training.abc244 import *
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
        input_text = """4
SSRS
"""
        expected = "2 -1\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """20
SRSRSSRSSSRSRRRRRSRR
"""
        expected = "0 1\n"
        self._run(input_text, expected, self.task)



class InputTestsD(BaseInputTests):
    task = TaskD()

    def test_1(self):
        input_text = """R G B
R G B
"""
        expected = "Yes\n"
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



class InputTestsE(BaseInputTests):
    task = TaskE()

    def test_1(self):
        input_text = """4 4 4 1 3 2
1 2
2 3
3 4
1 4
"""
        expected = "4\n"
        self._run(input_text, expected, self.task)