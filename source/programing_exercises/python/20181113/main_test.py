import unittest
from test.support import captured_stdout


def exectue():
    n = 100

    while n != 0:
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

        n = n - 1


def for_each():
    for n in range(100):
        print(n)


class MainTest(unittest.TestCase):

    def test_for_each(self):
        for_each()

    def test_1から100までプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[0], "Buzz")
        self.assertEqual(lines[99], "1")

    def test_3の倍数のときは数の代わりにFizzをプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[97], "Fizz")

    def test_5の倍数のときは数の代わりにBuzzをプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[95], "Buzz")

    def test_3と5の倍数のときは数の代わりにFizzBuzzをプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[85], "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
