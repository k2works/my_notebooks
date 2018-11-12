import unittest

class MainTest(unittest.TestCase):
  def test_初めの失敗するテスト(self):
    self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()