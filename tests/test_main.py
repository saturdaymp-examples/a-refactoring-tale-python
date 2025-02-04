import io
import sys
import unittest

from approvaltests import verify
from contextlib import redirect_stdout
from src.main import main

class MainTest(unittest.TestCase):
    def test_30_days(self):
        sys.argv = ['main.py', '30']
        result = io.StringIO()

        with redirect_stdout(result):
            main()

        verify(result.getvalue())

if __name__ == '__main__':
    unittest.main()
