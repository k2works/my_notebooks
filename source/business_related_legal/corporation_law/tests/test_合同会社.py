import unittest
from 会社.持分会社 import 持分会社
from 会社.合同会社 import 合同会社
from 会社.有限責任事業組合 import 有限責任事業組合
from 会社.株式会社 import 株式会社
from 資本.資本 import 金銭
from 資本.資本 import 信用
from 資本.資本 import 労務
from 社員.社員 import 無限責任社員
from 社員.社員 import 有限責任社員
from 社員.責任 import 間接責任
from 権利.権利 import 業務執行権


class 合同会社テスト(unittest.TestCase):
    def setUp(self):
        self._社員 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        self._会社 = 合同会社([self._社員])

    def test_合同会社は持分会社(self):
        self.assertTrue(issubclass(合同会社, 持分会社))

    def test_合同会社は有限責任社員のみで構成される(self):
        self.assertIn(self._会社.社員[0], [self._社員])

        with self.assertRaises(Exception) as cm:
            合同会社([無限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

    def test_合同会社は所有と経営が一致している(self):
        self.assertEqual(str(self._会社), '所有と経営が一致')

    def test_合同会社は法人格を持つ(self):
        self.assertTrue(self._会社.法人格)

    def test_合同会社の社員は原則として業務執行権を有し義務を負う(self):
        self.assertIn(業務執行権(), self._会社.社員[0].権利)

    def test_合同会社の出資は金銭等に限られ信用労務による出資はできない(self):
        社員 = 有限責任社員(間接責任, {'財産': 金銭(1), '信用': None, '労務': None})
        会社 = 合同会社([社員])
        self.assertIn(金銭(1), 会社.資本)

        社員 = 有限責任社員(間接責任, {'財産': None, '信用': 信用(), '労務': 労務()})
        with self.assertRaises(Exception) as cm:
            会社 = 合同会社([社員])
        self.assertEqual(cm.exception.args[0], '出資は金銭等に限られる')

    def test_合同の資本金は1円以上(self):
        社員 = 有限責任社員(間接責任(), {'財産': 金銭(0), '信用': None, '労務': None})
        with self.assertRaises(Exception) as cm:
            合同会社([社員])
        self.assertEquals(cm.exception.args[0], '資本金1円以上')

    def test_合同会社は株式会社に組織変更できる(self):
        社員 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        組織 = 株式会社([社員])
        self.assertEquals(self._会社.組織変更(組織), 組織)

    def test_合同会社は有限責任事業組合に組織変更できない(self):
        社員1 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        社員2 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        組織 = 有限責任事業組合([社員1, 社員2])
        with self.assertRaises(Exception) as cm:
            self._会社.組織変更(組織)
        self.assertEquals(cm.exception.args[0], '変更不可')
