from algorithm_training.sample import Task
from .base import BaseInputTests


class InputTests(BaseInputTests):
    def test_1(self):
        input_text = """aba"""
        expected = "aab\n"
        self._run(input_text, expected, Task())

    # def test_2(self):
    #     input_text = """2 3"""
    #     expected = "5\n"
    #     self._run(input_text, expected, Task())
