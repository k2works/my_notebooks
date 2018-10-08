import unittest
from 社員.社員 import 有限責任社員
from 社員.責任 import 間接責任
from 会社.株式会社 import 株式会社
from 登記.募集設立 import 募集設立
from 登記.発起設立 import 発起設立
from 資本.資本 import 不動産, 金銭
from 登記.定款 import 定款


class 会社設立テスト(unittest.TestCase):
    def setUp(self):
        _発起人 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        _出資者 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None},発起人=False)
        self._株式会社 = 株式会社([_発起人,_出資者])

    def test_発起設立では発起人が設立時に発行するすべての株式を引き受ける(self):
        _会社 = 発起設立(self._株式会社).実施()
        self.assertEquals(len(_会社.社員), 1)

    def test_発起設立では払込保証証明は不要(self):
        _会社 = 発起設立(self._株式会社).実施()
        self.assertFalse(_会社.払込金保管証明)

    def test_発起設立では創立総会は不要(self):
        _会社 = 発起設立(self._株式会社).実施()
        self.assertFalse(_会社.創立総会)

    def test_発起設立の設立登記は一定の日から2週間以内に行わなければならない(self):
        _会社 = 発起設立(self._株式会社).実施()
        self.assertEquals(_会社.設立登記, '発起人が定めた日から2週間以内')

    def test_発起設立では定款が作成される(self):
        _会社 = 発起設立(self._株式会社).実施()
        self.assertEquals(type(_会社.定款), 定款)

    def test_発起設立では現物出資ができる(self):
        _発起人1 = 有限責任社員(間接責任(), {'財産': 金銭(1_000_000), '信用': None, '労務': None})
        _発起人2 = 有限責任社員(間接責任(), {'財産': [金銭(5_000_000), 不動産(金銭(5_000_000))], '信用': None, '労務': None})
        _株式会社 = 株式会社([_発起人1, _発起人2])
        _会社 = 発起設立(_株式会社).実施()
        self.assertEquals(_会社.資本[0], 金銭(1_000_000))
        self.assertEquals(_会社.資本[1], 金銭(5_000_000))
        self.assertEquals(_会社.資本[2], 不動産(金銭(5_000_000)))
        self.assertEquals(_会社._資本金, 金銭(11_000_000))

    def test_募集設立では発起人が設立に発行するすべての株式を引き受けない(self):
        _会社 = 募集設立(self._株式会社).実施()
        self.assertNotEquals(len(_会社.社員), 1)

    def test_募集設立では払込保証証明は必要(self):
        _会社 = 募集設立(self._株式会社).実施()
        self.assertTrue(_会社.払込金保管証明)

    def test_募集設立では創立総会は必要(self):
        _会社 = 募集設立(self._株式会社).実施()
        self.assertTrue(_会社.創立総会)

    def test_募集設立の設立登記は一定の日から2週間以内に行わなければならない(self):
        _会社 = 募集設立(self._株式会社).実施()
        self.assertEquals(_会社.設立登記, '創立総会の終結の日の翌日から2週間以内')

    def test_募集設立では定款が作成される(self):
        _会社 = 募集設立(self._株式会社).実施()
        self.assertEquals(type(_会社.定款), 定款)

    def test_募集設立では現物出資ができるのは発起人に限られる(self):
        _発起人1 = 有限責任社員(間接責任(), {'財産': 金銭(1_000_000), '信用': None, '労務': None})
        _発起人2 = 有限責任社員(間接責任(), {'財産': 金銭(5_000_000), '信用': None, '労務': None})
        _出資者 = 有限責任社員(間接責任(), {'財産': [金銭(5_000_000), 不動産(金銭(5_000_000))], '信用': None, '労務': None}, 発起人=False)
        with self.assertRaises(Exception) as cm:
            _株式会社 = 株式会社([_発起人1, _発起人2, _出資者])
            _会社 = 募集設立(_株式会社).実施()
        self.assertEquals(cm.exception.args[0], '現物出資できるのは発起人に限られる')

