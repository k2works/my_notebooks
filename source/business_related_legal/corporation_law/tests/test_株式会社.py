import unittest
from 会社.会社 import 会社
from 会社.会社 import 物的会社
from 会社.持分会社 import 持分会社
from 会社.合同会社 import 合同会社
from 会社.有限責任事業組合 import 有限責任事業組合
from 会社.株式会社 import 株式会社
from 会社.株式会社 import 特例有限会社
from 資本.資本 import 金銭
from 社員.社員 import 無限責任社員
from 社員.社員 import 有限責任社員
from 社員.責任 import 直接責任
from 社員.責任 import 間接責任


class 株式会社テスト(unittest.TestCase):
    def setUp(self):
        self._社員 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        self._会社 = 株式会社([self._社員])

    def test_持分会社は会社(self):
        self.assertTrue(issubclass(持分会社, 会社))

    def test_株式会社は会社(self):
        self.assertTrue(issubclass(株式会社, 会社))

    def test_株式会社は物的会社(self):
        self.assertTrue(issubclass(株式会社, 物的会社))

    def test_株式会社は有限責任社員のみで構成される(self):
        self.assertIn(self._会社.社員[0], [self._社員])

        with self.assertRaises(Exception) as cm:
            株式会社([無限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

    def test_株式会社は所有と経営が分離(self):
        self.assertEqual(str(self._会社), '所有と経営が分離')

    def test_特例有限会社は株式会社(self):
        self.assertTrue(issubclass(特例有限会社, 株式会社))

    def test_H18有限責任会社廃止(self):
        with self.assertRaises(Exception) as cm:
            特例有限会社([有限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], 'H18有限会社法廃止')

    def test_株式会社の社員は退社制度が認められない(self):
        社員1 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        社員2 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        会社 = 株式会社([社員1, 社員2])
        with self.assertRaises(Exception) as cm:
            会社.退社制度(社員2)
        self.assertEquals(cm.exception.args[0], '退社制度は認められない')
        self.assertEqual(len(会社.社員), 2)

    def test_株式会社の社員は株式を譲渡して投下資本を回収できる(self):
        社員1 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        社員2 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        会社 = 株式会社([社員1, 社員2])
        self.assertEquals(len(会社.社員), 2)

    def test_株式会社の資本金は1円以上(self):
        社員 = 有限責任社員(間接責任(), {'財産': 金銭(0), '信用': None, '労務': None})
        with self.assertRaises(Exception) as cm:
            株式会社([社員])
        self.assertEquals(cm.exception.args[0], '資本金1円以上')

    def test_株式会社は合同会社に組織変更できる(self):
        社員 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        組織 = 合同会社([社員])
        self.assertEquals(self._会社.組織変更(組織), 組織)

    def test_株式会社は有限責任事業組合に組織変更できない(self):
        社員1 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        社員2 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        組織 = 有限責任事業組合([社員1, 社員2])
        with self.assertRaises(Exception) as cm:
            self._会社.組織変更(組織)
        self.assertEquals(cm.exception.args[0], '変更不可')
