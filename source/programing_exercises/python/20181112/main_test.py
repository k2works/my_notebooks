import unittest
from test.support import captured_stdout


class FizzBuzz():
    FIZZ = "Fizz"
    BUZZ = "Buzz"
    FIZZ_BUZZ = "FizzBuzz"
    __count = 0
    __values = []

    def __init__(self, count):
        self.__count = count

    def execute(self):
        self.__iterate(self.__count)

        for value in self.__values:
            print(value)

    @classmethod
    def is_fizz(cls, number):
        return number % 3 == 0

    @classmethod
    def is_fuzz(cls, number):
        return number % 5 == 0

    def __iterate(self, count):
        for n in range(count + 1):
            self.__values.append(self.__generate(n))

    def __generate(self, number):
        if self.is_fizz(number) and self.is_fuzz(number):
            return self.FIZZ_BUZZ
        elif self.is_fizz(number):
            return self.FIZZ
        elif self.is_fuzz(number):
            return self.BUZZ
        else:
            return number


class MainTest(unittest.TestCase):

    def test_結果を100回出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz(count=100)
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[1], "1")
        self.assertEqual(lines[-1], "Buzz")

    def test_3の倍数の時はFizzを出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz(count=10)
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[3], "Fizz")
        self.assertEqual(lines[6], "Fizz")

    def test_5の倍数の時はBuzzを出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz(count=10)
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[5], "Buzz")
        self.assertEqual(lines[10], "Buzz")

    def test_3と5の両方の倍数の時はFizzBuzzを出力する(self):
        with captured_stdout() as stdout:
            fizzBuzz = FizzBuzz(count=15)
            fizzBuzz.execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[15], "FizzBuzz")

    def test_isFizz(self):
        self.assertTrue(FizzBuzz.is_fizz(3))
        fizzBuzz = FizzBuzz(100)
        self.assertTrue(fizzBuzz.is_fizz(6))

    def test_isBuzz(self):
        self.assertTrue(FizzBuzz.is_fuzz(5))
        fizzBuzz = FizzBuzz(100)
        self.assertTrue(fizzBuzz.is_fuzz(10))


if __name__ == "__main__":
    unittest.main()
