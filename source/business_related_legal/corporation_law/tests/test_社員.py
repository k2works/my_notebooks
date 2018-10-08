import unittest
from 社員.社員 import 社員
from 社員.社員 import 無限責任社員
from 社員.社員 import 有限責任社員
from 社員.責任 import 直接責任
from 社員.責任 import 間接責任

class 社員テスト(unittest.TestCase):
    def test_無限責任社員(self):
        self.assertTrue(issubclass(無限責任社員, 社員))

    def test_直接無限責任社員(self):
        社員 = 無限責任社員(直接責任())
        self.assertEqual(type(社員.責任), 直接責任)

    def test_間接無限責任社員(self):
        社員 = 無限責任社員(間接責任())
        self.assertEqual(type(社員.責任), 間接責任)

    def test_有限責任社員(self):
        self.assertTrue(issubclass(有限責任社員, 社員))

    def test_直接有限責任社員(self):
        社員 = 有限責任社員(直接責任())
        self.assertEqual(type(社員.責任), 直接責任)

    def test_間接有限責任社員(self):
        社員 = 有限責任社員(間接責任())
        self.assertEqual(type(社員.責任), 間接責任)
