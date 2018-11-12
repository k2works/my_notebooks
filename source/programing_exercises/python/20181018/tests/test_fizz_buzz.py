import unittest
from fizz_buzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def test_3ならばFizzを返す(self):
        self.assertEqual(FizzBuzz.generate(3), 'Fizz')

    def test_6ならばFizzを返す(self):
        self.assertEqual(FizzBuzz.generate(6), 'Fizz')        

    def test_5ならばBuzzを返す(self):
        self.assertEqual(FizzBuzz.generate(5), 'Buzz')

    def test_10ならばBuzzを返す(self):
        self.assertEqual(FizzBuzz.generate(10), 'Buzz')        

    def test_50ならばBuzzを返す(self):
        self.assertEqual(FizzBuzz.generate(5), 'Buzz')        

    def test_15ならばFizzBuzzを返す(self):
        self.assertEqual(FizzBuzz.generate(15), 'FizzBuzz')

    def test_30ならばFizzBuzzを返す(self):
        self.assertEqual(FizzBuzz.generate(30), 'FizzBuzz')        

    def test_1ならば1を返す(self):
        self.assertEqual(FizzBuzz.generate(1), 1)

    def test_101ならば101を返す(self):
        self.assertEqual(FizzBuzz.generate(101), 101)        

    def test_5回実行されたならば配列を返す(self):
        self.assertEqual(FizzBuzz.iterate(5), [1, 2, 'Fizz', 4, 'Buzz'])

    def test_10回実行されたならば配列を返す(self):
        self.assertEqual(FizzBuzz.iterate(10), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'])


if __name__ == '__main__':
    unittest.main()