import unittest
from 会社.合資会社 import 合資会社
from 会社.持分会社 import 持分会社
from 資本.資本 import 財産
from 資本.資本 import 信用
from 資本.資本 import 労務
from 社員.社員 import 無限責任社員
from 社員.社員 import 有限責任社員
from 社員.責任 import 直接責任
from 権利.権利 import 業務執行権


class 合資会社テスト(unittest.TestCase):
    def test_合資会社は持分会社(self):
        self.assertTrue(issubclass(合資会社, 持分会社))

    def test_合資会社は有限責任社員と無限責任社員で構成される(self):
        社員1 = 有限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合資会社([社員1, 社員2])
        self.assertIn(会社.社員[0], [社員1])
        self.assertIn(会社.社員[1], [社員2])

        with self.assertRaises(Exception) as cm:
            合資会社([社員1])
        self.assertEqual(cm.exception.args[0], '構成員2名以上')

        with self.assertRaises(Exception) as cm:
            合資会社([社員1, 社員1])
        self.assertEqual(cm.exception.args[0], '無限責任社員が必要')

        with self.assertRaises(Exception) as cm:
            合資会社([社員2, 社員2])
        self.assertEqual(cm.exception.args[0], '有限責任社員が必要')

    def test_合資会社は所有と経営が一致している(self):
        社員1 = 有限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合資会社([社員1, 社員2])
        self.assertEqual(str(会社), '所有と経営が一致')

    def test_合資会社は法人格を持つ(self):
        社員1 = 有限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合資会社([社員1, 社員2])
        self.assertTrue(会社.法人格)

    def test_合資会社の各社員は原則として業務執行権を持つ(self):
        社員1 = 有限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合資会社([社員1, 社員2])
        self.assertIn(業務執行権(), 会社.社員[0].権利)
        self.assertIn(業務執行権(), 会社.社員[1].権利)

    def test_合資会社の直接有限責任社員の出資は金銭等に限られる(self):
        社員1 = 有限責任社員(直接責任(), {'財産': None, '信用': 信用(), '労務': None})
        社員2 = 無限責任社員(直接責任(), {'財産': 財産(), '信用': None, '労務': None})

        with self.assertRaises(Exception) as cm:
            会社 = 合資会社([社員1, 社員2])
        self.assertEqual(cm.exception.args[0], '直接有限責任社員の出資は金銭等に限られる')

    def test_合資会社の直接無限責任社員の出資は金銭等信用労務(self):
        社員1 = 有限責任社員(直接責任(), {'財産': 財産(), '信用': None, '労務': None})
        社員2 = 無限責任社員(直接責任(), {'財産': None, '信用': 信用(), '労務': 労務()})
        会社 = 合資会社([社員1, 社員2])
        self.assertIn(信用(), 会社.資本)
        self.assertIn(労務(), 会社.資本)

