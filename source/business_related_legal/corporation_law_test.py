import unittest
from corporation_law import *


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


class 会社テスト(unittest.TestCase):
    pass


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


class 定款テスト(unittest.TestCase):
    def setUp(self):
        self._定款 = 定款()

    def test_定款は絶対的記載事項を持つ(self):
        self.assertEqual(type(self._定款.絶対的記載事項), 絶対的記載事項)

    def test_定款の絶対的記載事項には会社の目的がある(self):
        self.assertEqual(self._定款.絶対的記載事項.会社の目的,'会社の事業目的を記載する')

    def test_定款の絶対的記載事項には商号がある(self):
        self.assertEqual(self._定款.絶対的記載事項.商号,'会社が自己を表すために用いる名称')

    def test_定款の絶対的記載事項には本店の所在地がある(self):
        self.assertEqual(self._定款.絶対的記載事項.本店の所在地,'最小行政区画（市町村／東京特別区）により記載')

    def test_定款の絶対的記載事項には設立に際して出資される財産の価格またはその最低額がある(self):
        self.assertEqual(self._定款.絶対的記載事項.設立に際して出資される財産の価格またはその最低額,'これに記載された額以上の財産が現実に出資されなければならない')

    def test_定款の絶対的記載事項には発起人の氏名または名称および住所がある(self):
        self.assertEqual(self._定款.絶対的記載事項.発起人の氏名または名称および住所,'これに記載されたものが発起人となる')

    def test_定款の絶対的記載事項には発行可能株式総数がある(self):
        self.assertEqual(self._定款.絶対的記載事項.発行可能株式総数,'株主総会の決議によらず、取締役会の決議だけで発行することが株式数で、この上限の範囲内であれば、取締役会で自由に株式を発行できる')
                
    def test_定款は相対的記載事項を持つ(self):
        self.assertEqual(type(self._定款.相対的記載事項), 相対的記載事項)

    def test_定款の相対的記載事項には変態設立事項がある(self):
        self.assertEqual(type(self._定款.相対的記載事項.変態設立事項),変態設立事項)

    def test_変態設立事項には現物出資がある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.現物出資,'金銭以外の財産をもってする出資')

    def test_変態設立事項には財産引受けがある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.財産引受け, '会社のために会社の成立を条件として特定の財産を譲り受けることを約する契約')

    def test_変態設立事項には発起人の報酬その他の特別の利益がある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.発起人の報酬その他の特別の利益, '設立中の会社の機関として行った労務に対する報酬その他の利益')

    def test_変態設立事項には発起人の設立費用がある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.設立費用,'会社設立に必要な取引行為から生じる費用のうち、会社が負担すべきもの')

    def test_定款は任意的記載事項を持つ(self):
        self.assertEqual(type(self._定款.任意的記載事項), 任意的記載事項)


if __name__ == '__main__':
    unittest.main()
