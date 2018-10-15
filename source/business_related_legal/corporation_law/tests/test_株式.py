import unittest
from 資本.株式 import 株式
from 資本.株式 import 自益権
from 資本.株式 import 共益権
from 資本.株式 import 単独株主権
from 資本.株式 import 少数株主権
from 資本.種類株式 import 優先株
from 資本.種類株式 import 劣後株
from 資本.種類株式 import 議決権制限株式
from 資本.種類株式 import 取得請求権付株式
from 資本.種類株式 import 取得条項付株式
from 資本.種類株式 import 全部取得条項付種類株式
from 資本.種類株式 import 拒否権付株式
from 会社.株式会社 import 株式会社
from 社員.社員 import 有限責任社員
from 社員.責任 import 間接責任
from 資本.資本 import 金銭
from 登記.発起設立 import 発起設立


class 株式テスト(unittest.TestCase):
    def setUp(self):
        self.__株式 = 株式(1)

    def test_株式は細分化された均一的な割合単位(self):
        self.assertEqual(str(self.__株式), '1株')

    def test_持ち分は社員の出資の額に応じて異なる単位(self):
        pass

    def test_株主は自益権を持つ(self):
        self.assertEqual(type(self.__株式.自益権), 自益権)

    def test_株主は共益権を持つ(self):
        self.assertEqual(type(self.__株式.共益権), 共益権)

    def test_共益権には単独株主権と少数株主権がある(self):
        共益権 = self.__株式.共益権
        self.assertEqual(type(共益権.単独株主権), 単独株主権)
        self.assertEqual(type(共益権.少数株主権), 少数株主権)


class 種類株式テスト(unittest.TestCase):
    def setUp(self):
        self.__優先株 = 優先株(1)
        self.__劣後株 = 劣後株(1)
        self.__議決権制限株式 = 議決権制限株式(1)
        self.__取得請求権付株式 = 取得請求権付株式(1)
        self.__取得条項付株式 = 取得条項付株式(1)
        self.__全部取得条項付種類株式 = 全部取得条項付種類株式(1)
        self.__拒否権付株式 = 拒否権付株式(1)

    def test_種類株式には優先株がある(self):
        self.assertEqual(type(self.__優先株), 優先株)
        self.assertEqual(str(self.__優先株), '他の株式に比べて優先的取扱を受ける株式')

    def test_種類株式には劣後株がある(self):
        self.assertEqual(type(self.__劣後株), 劣後株)
        self.assertEqual(str(self.__劣後株), '配当や残余財産の分配について、他の株式に比べて劣後的内容を持つ株式')

    def test_種類株式には議決権制限株式がある(self):
        self.assertEqual(type(self.__議決権制限株式), 議決権制限株式)
        self.assertEqual(str(self.__議決権制限株式), '全部議決権制限株式と一部議決権制限株式')

    def test_議決権制限株式は公開会社では発行済株式総数の2分の1までに制限(self):
        pass

    def test_議決権制限株式は非公開会社では制限なし(self):
        pass

    def test_種類株式には取得請求権付株式がある(self):
        self.assertEqual(type(self.__取得請求権付株式), 取得請求権付株式)
        self.assertEqual(str(self.__取得請求権付株式), '株主がその株式会社に対して株式の取得を請求することができる株式')

    def test_種類株式には所得条項付株式がある(self):
        self.assertEqual(type(self.__取得条項付株式), 取得条項付株式)
        self.assertEqual(str(self.__取得条項付株式), '株式会社が一定の事由が生じたことを条件として強制的にその株式を株主から取得することができる株式')

    def tset_種類株式には全部取得条項付株式がある(self):
        self.assertEqual(type(self.__全部取得条項付種類株式), 全部取得条項付種類株式)
        self.assertEqual(str(self.__全部取得条項付種類株式),
                         "2つ以上の種類株式発行会社が株主総会の特別決議によってそのうちの1つの種類株式の全部またはは複数の種類株式のの全部を取得することができる株式"
                         )

    def test_種類株式には拒否権付株式がある(self):
        self.assertEqual(type(self.__拒否権付株式), 拒否権付株式)
        self.assertEqual(str(self.__拒否権付株式), '株主総会等の決議のほか当該種類株式の種類株主総会の決議を必要とする株式')


class 株式の譲渡テスト(unittest.TestCase):
    def setUp(self):
        発起人 = 有限責任社員(間接責任(), {'財産': 金銭(1), '信用': None, '労務': None})
        self.__株式会社 = 株式会社([発起人])

    def test_非公開会社は発行株式の全部に譲渡制限を定めている(self):
        self.__会社 = 発起設立(self.__株式会社).実施(種類株式=議決権制限株式)
        社員 = self.__会社.社員
        self.assertEqual(type(社員[0].株式[0]), 議決権制限株式)

    def test_公開会社は発行株式の全部に譲渡制限を定めていない(self):
        pass

    def test_公開会社は発行株式の一部に譲渡制限を定めている(self):
        pass

    def test_株式の譲渡の承認機関は株主総会の普通決議(self):
        pass

    def test_株式の譲渡の承認機関は2週間以内(self):
        pass

    def test_株式の譲渡の売買価格の決定は20日以内(self):
        pass
