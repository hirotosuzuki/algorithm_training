from algorithm_training.problem_a import Task
from .base import BaseInputTests


class InputTests(BaseInputTests):
    def test_1(self):
        input_text = """30 500 20 103"""
        expected = "0.042553191489\n"
        self._run(input_text, expected, Task())

    # def test_2(self):
    #     input_text = """2 3"""
    #     expected = "5\n"
    #     self._run(input_text, expected, Task())
