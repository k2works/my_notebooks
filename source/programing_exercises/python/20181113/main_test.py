import unittest
from test.support import captured_stdout


def exectue():
    print("1")


class MainTest(unittest.TestCase):

    def test_1から100までプリントする(self):
        with captured_stdout() as stdout:
            exectue()

        self.assertEqual(stdout.getvalue(), "1\n")


if __name__ == "__main__":
    unittest.main()
