from algorithm_training.abc243 import *
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