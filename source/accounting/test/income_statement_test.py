import unittest
from src.income_statement import *


class Test損益計算書(unittest.TestCase):
    def setUp(self):
        _売上高 = 売上高(10000)
        _売上原価 = 売上原価(3000)
        _販管費内訳 = [
            給料賃金(500),
            福利厚生費(500),
            広告宣伝費(500),
            水道光熱費(500),
            交際費(500),
            保険料(500),
            支払家賃(500),
            減価償却費(500)
        ]
        _販管費 = 販管費(_販管費内訳)
        _営業外収益内訳 = [
            受取利息(50),
            受取配当金(50),
            有価証券評価益(50),
            有価証券売却益(50),
            受取家賃(50),
            仕入割引(50)
        ]
        _営業外収益 = 営業外収益(_営業外収益内訳)
        _営業外費用内訳 = [
            支払利息(100),
            手形売却損(100),
            有価証券評価損(100),
            有価証券売却損(100),
            売上割引(100)
        ]
        _営業外費用 = 営業外費用(_営業外費用内訳)
        _特別利益内訳 = [
            固定資産売却益(0),
            国庫補助金受贈益(0)
        ]
        _特別利益 = 特別利益(_特別利益内訳)
        _特別損失内訳 = [
            固定資産売却損(0),
            災害損失(0)
        ]
        _特別損失 = 特別損失(_特別損失内訳)
        self.損益計算書 = 損益計算書(_売上高, _売上原価, _販管費, _営業外収益, _営業外費用, _特別利益, _特別損失)

    def test損益計算書(self):
        self.assertEqual(損益計算書, type(self.損益計算書))

    def test損益計算書は売上高を持つ(self):
        self.assertEqual(売上高, type(self.損益計算書.売上高))

    def test損益計算書は売上原価を持つ(self):
        self.assertEqual(売上原価, type(self.損益計算書.売上原価))

    def test損益計算書は販売費および一般管理費を持つ(self):
        self.assertEqual(販管費, type(self.損益計算書.販管費))

    def test損益計算書は営業外収益を持つ(self):
        self.assertEqual(営業外収益, type(self.損益計算書.営業外収益))

    def test損益計算書は営業外費用を持つ(self):
        self.assertEqual(営業外費用, type(self.損益計算書.営業外費用))

    def test損益計算書は特別利益を持つ(self):
        self.assertEqual(特別利益, type(self.損益計算書.特別利益))

    def test損益計算書は特別損失を持つ(self):
        self.assertEqual(特別損失, type(self.損益計算書.特別損失))

    def test損益計算書は売上総利益を計算する(self):
        self.assertEqual(7000, self.損益計算書.売上総利益.金額)

    def test損益計算書は営業利益を計算する(self):
        self.assertEqual(3000, self.損益計算書.営業利益.金額)

    def test損益計算書は経常利益を計算する(self):
        self.assertEqual(2800, self.損益計算書.経常利益.金額)

    def test損益計算書は税引前当期純利益を計算する(self):
        self.assertEqual(2800, self.損益計算書.税引前当期純利益.金額)

    def test損益計算書は法人税等を計算する(self):
        self.assertEqual(1120, self.損益計算書.法人税等.金額)

    def test損益計算書は当期純利益を計算する(self):
        self.assertEqual(1680, self.損益計算書.当期純利益.金額)


if __name__ == "__main__":
    unittest.main()
