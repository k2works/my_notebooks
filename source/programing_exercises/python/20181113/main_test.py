import unittest
from test.support import captured_stdout


def exectue():
    iterate(100)


def iterate(count):
    for number in range(count + 1):
        print(generate(number))

def generate(number):
    value = str(number)
    if number % 3 == 0 and number % 5 == 0:
        value = "FizzBuzz"
    elif number % 3 == 0:
        value = "Fizz"
    elif number % 5 == 0:
        value = "Buzz"

    return value


class MainTest(unittest.TestCase):

    def test_1から100までプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[1], "1")
        self.assertEqual(lines[100], "Buzz")

    def test_3の倍数のときは数の代わりにFizzをプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[3], "Fizz")

    def test_5の倍数のときは数の代わりにBuzzをプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[5], "Buzz")

    def test_3と5の倍数のときは数の代わりにFizzBuzzをプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[15], "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
