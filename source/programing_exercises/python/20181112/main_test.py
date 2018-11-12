import unittest
from test.support import captured_stdout


def execute():        
    for n in range(100):
        num = n + 1
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")        
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def iterate(count):
    for n in range(count):
        print(n)

class MainTest(unittest.TestCase):

    def test_iterate(self):
        self.assertEqual(iterate(10), "")

    def test_結果を100回出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[0], "1")
        self.assertEqual(lines[99], "Buzz")

    def test_3の倍数の時はFizzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[2], "Fizz")
        self.assertEqual(lines[5], "Fizz")

    def test_5の倍数の時はBuzzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[4], "Buzz")
        self.assertEqual(lines[9], "Buzz")

    def test_3と5の両方の倍数の時はFizzBuzzを出力する(self):
        with captured_stdout() as stdout:
            execute()

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[14], "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
