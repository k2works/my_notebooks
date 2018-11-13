import unittest
from test.support import captured_stdout

FIZZ_BUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"
data = {
    'values': []
}


def exectue(count=100):

    iterate(count)

    for value in data['values']:
        print(value)


def iterate(count):
    for number in range(count + 1):
        value = generate(number)
        data['values'].append(value)


def generate(number):
    value = str(number)

    if number % 3 == 0 and number % 5 == 0:
        value = FIZZ_BUZZ
    elif number % 3 == 0:
        value = FIZZ
    elif number % 5 == 0:
        value = BUZZ

    return value


class MainTest(unittest.TestCase):

    def test_1から100までプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[1], "1")
        self.assertEqual(lines[100], "Buzz")

    def test_1から10までプリントする(self):
        with captured_stdout() as stdout:
            exectue(10)
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[10], "Buzz")
        

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
