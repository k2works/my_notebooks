import unittest


def execute():
  pass

class MainTest(unittest.TestCase):
  def test_結果を１００回出力する(self):
    self.assertTrue("1", execute())

if __name__ == "__main__":
    unittest.main()