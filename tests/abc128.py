from algorithm_training.abc128 import *
from .base import BaseInputTests

# class InputTestsA(BaseInputTests):
#     task = TaskA()

#     def test_1(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)

#     def test_2(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)

#     def test_3(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)

# class InputTestsB(BaseInputTests):
#     task = TaskB()

#     def test_1(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)

#     def test_2(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)

#     def test_3(self):
#         input_text = """"""
#         expected = "\n"
#         self._run(input_text, expected, self.task)


class InputTestsC(BaseInputTests):
    task = TaskC()

    def test_1(self):
        input_text = """2 2
2 1 2
1 2
0 1
"""
        expected = "1\n"
        self._run(input_text, expected, self.task)

    def test_2(self):
        input_text = """2 3
2 1 2
1 1
1 2
0 0 1
"""
        expected = "0\n"
        self._run(input_text, expected, self.task)

    def test_3(self):
        input_text = """5 2
3 1 2 5
2 2 3
1 0
"""
        expected = "8\n"
        self._run(input_text, expected, self.task)