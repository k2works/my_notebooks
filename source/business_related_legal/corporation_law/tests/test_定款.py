import unittest
from 登記.定款 import 定款
from 登記.定款 import 絶対的記載事項
from 登記.定款 import 相対的記載事項, 変態設立事項
from 登記.定款 import 任意的記載事項


class 定款テスト(unittest.TestCase):
    def setUp(self):
        self._定款 = 定款()

    def test_定款は絶対的記載事項を持つ(self):
        self.assertEqual(type(self._定款.絶対的記載事項), 絶対的記載事項)

    def test_定款の絶対的記載事項には会社の目的がある(self):
        self.assertEqual(self._定款.絶対的記載事項.会社の目的, '会社の事業目的を記載する')

    def test_定款の絶対的記載事項には商号がある(self):
        self.assertEqual(self._定款.絶対的記載事項.商号, '会社が自己を表すために用いる名称')

    def test_定款の絶対的記載事項には本店の所在地がある(self):
        self.assertEqual(self._定款.絶対的記載事項.本店の所在地, '最小行政区画（市町村／東京特別区）により記載')

    def test_定款の絶対的記載事項には設立に際して出資される財産の価格またはその最低額がある(self):
        self.assertEqual(self._定款.絶対的記載事項.設立に際して出資される財産の価格またはその最低額, 'これに記載された額以上の財産が現実に出資されなければならない')

    def test_定款の絶対的記載事項には発起人の氏名または名称および住所がある(self):
        self.assertEqual(self._定款.絶対的記載事項.発起人の氏名または名称および住所, 'これに記載されたものが発起人となる')

    def test_定款の絶対的記載事項には発行可能株式総数がある(self):
        self.assertEqual(self._定款.絶対的記載事項.発行可能株式総数, '株主総会の決議によらず、取締役会の決議だけで発行することが株式数で、この上限の範囲内であれば、取締役会で自由に株式を発行できる')

    def test_定款は相対的記載事項を持つ(self):
        self.assertEqual(type(self._定款.相対的記載事項), 相対的記載事項)

    def test_定款の相対的記載事項には変態設立事項がある(self):
        self.assertEqual(type(self._定款.相対的記載事項.変態設立事項), 変態設立事項)

    def test_変態設立事項には現物出資がある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.現物出資, '金銭以外の財産をもってする出資')

    def test_変態設立事項には財産引受けがある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.財産引受け, '会社のために会社の成立を条件として特定の財産を譲り受けることを約する契約')

    def test_変態設立事項には発起人の報酬その他の特別の利益がある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.発起人の報酬その他の特別の利益, '設立中の会社の機関として行った労務に対する報酬その他の利益')

    def test_変態設立事項には発起人の設立費用がある(self):
        self.assertEqual(self._定款.相対的記載事項.変態設立事項.設立費用, '会社設立に必要な取引行為から生じる費用のうち、会社が負担すべきもの')

    def test_定款は任意的記載事項を持つ(self):
        self.assertEqual(type(self._定款.任意的記載事項), 任意的記載事項)
