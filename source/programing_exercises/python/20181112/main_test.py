import unittest
from test.support import captured_stdout

data = {'count': 100, 'values': []}


def execute():
    iterate(data['count'])

    for value in data['values']:
        print(value)


def iterate(count):
    for n in range(count + 1):
        data['values'].append(generate(n))


def generate(number):
    if isFizz(number) and isBuzz(number):
        return "FizzBuzz"
    elif isFizz(number):
        return "Fizz"
    elif isBuzz(number):
        return "Buzz"
    else:
        return number

def isFizz(number):
    return number % 3 == 0

def isBuzz(number):
    return number % 5 == 0


class MainTest(unittest.TestCase):

    def test_結果を100回出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[1], "1")
        self.assertEqual(lines[100], "Buzz")

    def test_3の倍数の時はFizzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[3], "Fizz")
        self.assertEqual(lines[6], "Fizz")

    def test_5の倍数の時はBuzzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[5], "Buzz")
        self.assertEqual(lines[10], "Buzz")

    def test_3と5の両方の倍数の時はFizzBuzzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[15], "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
