import unittest
from test.support import captured_stdout


def exectue():
    n = 100

    while n != 0:
        if n % 3 == 0:
            print("Fizz")
        else:
            print(n)
        
        n = n - 1


class MainTest(unittest.TestCase):

    def test_1から100までプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[0], "100")
        self.assertEqual(lines[99], "1")

    def test_3の倍数のときは数の代わりにFizzをプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[97], "Fizz")


if __name__ == "__main__":
    unittest.main()
