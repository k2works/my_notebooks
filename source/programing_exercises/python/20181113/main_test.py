import unittest


def exectue():
    return "1"


class MainTest(unittest.TestCase):

    def test_1から100までプリントする(self):
        self.assertTrue(exectue(), "1")


if __name__ == "__main__":
    unittest.main()
