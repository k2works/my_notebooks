import unittest
from test.support import captured_stdout

data = {'count': 100, 'values': []}
FIZZ = "Fizz"
BUZZ = "Buzz"
FIZZ_BUZZ = "FizzBuzz"


class FizzBuzz():

    @classmethod
    def execute(cls):
        FizzBuzz.iterate(data['count'])

        for value in data['values']:
            print(value)
    
    @classmethod
    def iterate(cls, count):
        for n in range(count + 1):
            data['values'].append(FizzBuzz.generate(n))

    @classmethod
    def generate(cls, number):
        if FizzBuzz.isFizz(number) and FizzBuzz.isBuzz(number):
            return FIZZ_BUZZ
        elif FizzBuzz.isFizz(number):
            return FIZZ
        elif FizzBuzz.isBuzz(number):
            return BUZZ
        else:
            return number

    @classmethod
    def isFizz(cls, number):
        return number % 3 == 0

    @classmethod
    def isBuzz(cls, number):
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
