from algorithm_training.abc243 import *
from .base import BaseInputTests


class InputTestsA(BaseInputTests):
    def test_1(self):
        input_text = """25 10 11 12"""
        expected = "T\n"
        self._run(input_text, expected, TaskA())

    def test_2(self):
        input_text = """30 10 10 10"""
        expected = "F\n"
        self._run(input_text, expected, TaskA())

    def test_3(self):
        input_text = """100000 1 1 1"""
        expected = "M\n"
        self._run(input_text, expected, TaskA())

class InputTestsB(BaseInputTests):
    task = TaskB()

    def test_1(self):
        input_text = """4
        1 3 5 2
        2 3 1 4
        """
        expected = "1\n2\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """3
        1 2 3
        4 5 6
        """
        expected = "0\n0\n"
        self._run(input_text, expected, self.task)

    def test_3(self):
        input_text = """7
        4 8 1 7 9 5 6
        3 5 1 7 8 2 6
        """
        expected = "3\n2\n"
        self._run(input_text, expected, self.task)

class InputTestsC(BaseInputTests):
    task = TaskC()

    def test_1(self):
        input_text = """3
2 3
1 1
4 1
RRL
        """
        expected = "Yes\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """2
1 1
2 1
RR
        """
        expected = "No\n"
        self._run(input_text, expected, self.task)

    def test_3(self):
        input_text = """10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR
        """
        expected = "Yes\n"
        self._run(input_text, expected, self.task)