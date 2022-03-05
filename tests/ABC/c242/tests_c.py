from algorithm_training.ABC.c242.problem_c_retry import Task
from tests.base import BaseInputTests


class InputTests(BaseInputTests):
    def test_1(self):
        input_text = """4"""
        expected = "203\n"
        self._run(input_text, expected, Task())

    # def test_2(self):
    #     input_text = """3"""
    #     expected = "\n"
    #     self._run(input_text, expected, Task())

    def test_3(self):
        input_text = """2"""
        expected = "25\n"
        self._run(input_text, expected, Task())

    def test_4(self):
        input_text = """1000000"""
        expected = "248860093\n"
        self._run(input_text, expected, Task())
