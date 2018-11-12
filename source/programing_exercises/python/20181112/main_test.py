import unittest
from test.support import captured_stdout


def execute():
    n = 100
    while n != 0:
        print(n)
        n = n - 1


class MainTest(unittest.TestCase):

    def test_結果を１００回出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[99], "1")
        self.assertEqual(lines[0], "100")


if __name__ == "__main__":
    unittest.main()
