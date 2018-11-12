import unittest
from test.support import captured_stdout


def execute():
    n = 100
    while n != 0:
        if n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
        n = n - 1


class MainTest(unittest.TestCase):

    def test_結果を１００回出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[99], "1")
        self.assertEqual(lines[0], "Buzz")

    def test_３の倍数の時はFizzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[97], "Fizz")
        self.assertEqual(lines[94], "Fizz")

    def test_５の倍数の時はBuzzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[95], "Buzz")
        self.assertEqual(lines[90], "Buzz")


if __name__ == "__main__":
    unittest.main()
