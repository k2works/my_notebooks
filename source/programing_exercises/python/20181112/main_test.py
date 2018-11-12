import unittest
from test.support import captured_stdout


class FizzBuzz():
    FIZZ = "Fizz"
    BUZZ = "Buzz"
    FIZZ_BUZZ = "FizzBuzz"
    __data = {'count': 100, 'values': []}

    def execute(self):
        self.__iterate(self.__data['count'])

        for value in self.__data['values']:
            print(value)

    @classmethod
    def isFizz(cls, number):
        return number % 3 == 0

    @classmethod
    def isBuzz(cls, number):
        return number % 5 == 0

    def __iterate(self, count):
        for n in range(count + 1):
            self.__data['values'].append(self.__generate(n))

    def __generate(self, number):
        if self.isFizz(number) and self.isBuzz(number):
            return self.FIZZ_BUZZ
        elif self.isFizz(number):
            return self.FIZZ
        elif self.isBuzz(number):
            return self.BUZZ
        else:
            return number


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

    def test_isFizz(self):
        self.assertTrue(FizzBuzz.isFizz(3))
        fizzBuzz = FizzBuzz()        
        self.assertTrue(fizzBuzz.isFizz(6))

    def test_isBuzz(self):
        self.assertTrue(FizzBuzz.isBuzz(5))
        fizzBuzz = FizzBuzz()        
        self.assertTrue(fizzBuzz.isBuzz(10))


if __name__ == "__main__":
    unittest.main()
