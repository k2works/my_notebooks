import unittest
from test.support import captured_stdout


class FizzBuzz():
    data = {'count': 100, 'values': []}
    FIZZ = "Fizz"
    BUZZ = "Buzz"
    FIZZ_BUZZ = "FizzBuzz"

    def execute(self):
        self.iterate(self.data['count'])

        for value in self.data['values']:
            print(value)

    def iterate(self, count):
        for n in range(count + 1):
            self.data['values'].append(self.generate(n))

    def generate(self, number):
        if self.isFizz(number) and self.isBuzz(number):
            return self.FIZZ_BUZZ
        elif self.isFizz(number):
            return self.FIZZ
        elif self.isBuzz(number):
            return self.BUZZ
        else:
            return number

    def isFizz(self, number):
        return number % 3 == 0

    def isBuzz(self, number):
        return number % 5 == 0


class MainTest(unittest.TestCase):

    def test_結果を100回出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz()
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[1], "1")
        self.assertEqual(lines[100], "Buzz")

    def test_3の倍数の時はFizzを出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz()
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[3], "Fizz")
        self.assertEqual(lines[6], "Fizz")

    def test_5の倍数の時はBuzzを出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz()
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[5], "Buzz")
        self.assertEqual(lines[10], "Buzz")

    def test_3と5の両方の倍数の時はFizzBuzzを出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz()
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[15], "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
