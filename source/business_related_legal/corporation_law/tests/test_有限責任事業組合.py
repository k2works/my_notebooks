import unittest
from 会社.持分会社 import 持分会社
from 会社.合同会社 import 合同会社
from 会社.有限責任事業組合 import 有限責任事業組合
from 会社.株式会社 import 株式会社
from 資本.資本 import 金銭
from 社員.社員 import 無限責任社員
from 社員.社員 import 有限責任社員
from 社員.責任 import 直接責任
from 社員.責任 import 間接責任

class 有限責任事業組合テスト(unittest.TestCase):
    def setUp(self):
        self._社員1 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        self._社員2 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        self._会社 = 有限責任事業組合([self._社員1, self._社員2])

    def test_有限責任事業組合は持分会社(self):
        self.assertTrue(issubclass(有限責任事業組合, 持分会社))

    def test_有限責任事業組合は所有と経営が一致している(self):
        self.assertEqual(str(self._会社), '所有と経営が一致')

    def test_有限責任事業組合は有限責任社員2名以上で構成される(self):
        self.assertEqual(len(self._会社.社員), 2)

        with self.assertRaises(Exception) as cm:
            有限責任事業組合([有限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], '構成員2名以上')

        with self.assertRaises(Exception) as cm:
            有限責任事業組合([有限責任社員(間接責任()), 無限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

        with self.assertRaises(Exception) as cm:
            有限責任事業組合([有限責任社員(間接責任()), 無限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

    def test_有限責任事業組合は法人格を持たない(self):
        self.assertFalse(self._会社.法人格)

    def test_有限責任事業組合の資本金は2円以上(self):
        社員1 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        社員2 = 有限責任社員(間接責任(), {'財産': 金銭(0), '信用': None, '労務': None})
        with self.assertRaises(Exception) as cm:
            有限責任事業組合([社員1, 社員2])
        self.assertEquals(cm.exception.args[0], '資本金2円以上')

    def test_有限責任事業組合は株式会社に組織変更できない(self):
        社員 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        組織 = 株式会社([社員])
        with self.assertRaises(Exception) as cm:
            self._会社.組織変更(組織)
        self.assertEquals(cm.exception.args[0], '変更不可')

    def test_有限責任事業組合は合同会社に組織変更できない(self):
        社員1 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        社員2 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        組織 = 合同会社([社員1, 社員2])
        with self.assertRaises(Exception) as cm:
            self._会社.組織変更(組織)
        self.assertEquals(cm.exception.args[0], '変更不可')
