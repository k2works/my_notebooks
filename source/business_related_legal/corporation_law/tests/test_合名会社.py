import unittest
from 会社.合名会社 import 合名会社
from 会社.持分会社 import 持分会社
from 資本.資本 import 財産
from 資本.資本 import 信用
from 資本.資本 import 労務
from 社員.社員 import 無限責任社員
from 社員.社員 import 有限責任社員
from 社員.責任 import 直接責任
from 権利.権利 import 業務執行権
from 権利.権利 import 会社代表権


class 合名会社テスト(unittest.TestCase):
    def test_合名会社は持分会社(self):
        self.assertTrue(issubclass(合名会社, 持分会社))

    def test_合名会社は無限責任社員のみで構成される(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertIn(会社.社員[0], [社員])

        with self.assertRaises(Exception) as cm:
            合名会社([有限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '無限責任社員のみ')

    def test_合名会社は所有と経営が一致している(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertEqual(str(会社), '所有と経営が一致')

    def test_合名会社は法人格を持つ(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertTrue(会社.法人格)

    def test_合名会社は権利義務の帰属主体となる(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertTrue(会社.権利義務の帰属主体())

    def test_合名会社の社員は業務執行権と会社代表権を持つ(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertIn(業務執行権(), 会社.社員[0].権利)
        self.assertIn(会社代表権(), 会社.社員[0].権利)

    def test_合名会社の出資の目的は財産信用労務のいずれでも良い(self):
        _財産 = 財産()
        _信用 = 信用()
        _労務 = 労務()
        社員 = 無限責任社員(直接責任(),{'財産':_財産, '信用':_信用, '労務':_労務})
        会社 = 合名会社([社員])
        self.assertIn(_財産, 会社.資本)
        self.assertIn(_信用, 会社.資本)
        self.assertIn(_労務, 会社.資本)

    def test_合名会社の社員は退社制度が認められる(self):
        社員1 = 無限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合名会社([社員1, 社員2])
        会社.退社制度(社員1)
        self.assertIn(会社.社員[0], [社員2])

    def test_合名会社の社員は他の社員の承諾がない限り原則として持分の譲渡はできない(self):
        社員1 = 無限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        社員3 = 無限責任社員(直接責任())
        会社 = 合名会社([社員1, 社員2, 社員3])
        with self.assertRaises(Exception) as cm:
            会社.持分の譲渡(社員1)
        self.assertEqual(cm.exception.args[0], '持分の譲渡はできない')