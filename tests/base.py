import contextlib
import unittest


class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"


class BaseInputTests(unittest.TestCase):
    def _run(self, input_text, output_text, task):
        from io import StringIO
        buf_stdin = StringIO()
        buf_stdout = StringIO()

        buf_stdin.write(input_text)
        buf_stdin.seek(0)

        with redirect_stdin(buf_stdin), contextlib.redirect_stdout(buf_stdout):
            task.run()

        actual = buf_stdout.getvalue()
        expected = output_text
        self.assertEqual(actual, expected)
