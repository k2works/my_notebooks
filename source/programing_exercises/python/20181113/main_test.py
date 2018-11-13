import unittest
from test.support import captured_stdout


def exectue():
    n = 100

    while n != 0:
        print(n)
        n = n - 1


class MainTest(unittest.TestCase):

    def test_1から100までプリントする(self):
        with captured_stdout() as stdout:
            exectue()
            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[0], "100")                
        self.assertEqual(lines[99], "1")        


if __name__ == "__main__":
    unittest.main()
