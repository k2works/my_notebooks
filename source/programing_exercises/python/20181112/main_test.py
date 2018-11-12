import unittest
from test.support import captured_stdout


def execute():
    n = 100
    while n != 0:
        if n == 3:
            print("Fizz")
        else:
            print(n)
        n = n - 1


class MainTest(unittest.TestCase):

    def test_結果を１００回出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[99], "1")
        self.assertEqual(lines[0], "100")

    def test_３の倍数の時はFizzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[97], "Fizz")


if __name__ == "__main__":
    unittest.main()
