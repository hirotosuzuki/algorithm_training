from algorithm_training.problem_b import Task
from .base import BaseInputTests


class InputTests(BaseInputTests):
    def test_1(self):
        input_text = """aba"""
        expected = "aab\n"
        self._run(input_text, expected, Task())

    def test_2(self):
        input_text = """zzzz"""
        expected = "zzzz\n"
        self._run(input_text, expected, Task())
