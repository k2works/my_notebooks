class 会社:
    pass


class 物的会社(会社):
    def __str__(self):
        return "所有と経営が分離"


class 人的会社(会社):
    def __str__(self):
        return "所有と経営が一致"


class 持分会社(人的会社):
    _社員 = []
    _資本 = []

    def __init__(self, 社員構成):
        self._社員 = 社員構成
        self._法人格 = True

    @property
    def 社員(self):
        return self._社員

    @property
    def 法人格(self):
        return self._法人格

    @property
    def 資本(self):
        return self._資本

    def 権利義務の帰属主体(self):
        return self._法人格


class 株式会社(物的会社):
    _社員 = []
    _資本 = []

    def __init__(self, 社員構成, 払込金保管証明=False, 創立総会=False, 設立登記=None, 定款=None):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')

        self._社員 = 社員構成
        self._法人格 = True
        self._定款認証 = True
        self._決算公告義務 = True
        self._存続期間 = False
        self._払込金保管証明 = 払込金保管証明
        self._創立総会 = 創立総会
        self._設立登記 = 設立登記
        self._定款 = 定款

        self._資本 = []

        for 社員 in self._社員:
            _出資 = 社員.出資('財産')
            if type(_出資) is list:
                for 資本 in _出資:
                    self._資本.append(資本)
            else:
                self._資本.append(_出資)
        self._資本金()

    @property
    def 社員(self):
        return self._社員

    @property
    def 法人格(self):
        return self._法人格

    @property
    def 資本(self):
        return self._資本

    @property
    def 払込金保管証明(self):
        return self._払込金保管証明

    @property
    def 創立総会(self):
        return self._創立総会

    @property
    def 設立登記(self):
        return self._設立登記

    @property
    def 定款(self):
        return self._定款

    def 退社制度(self, 社員):
        raise Exception('退社制度は認められない')

    def 株式の譲渡(self, 譲渡する社員):
        self.__社員.remove(譲渡する社員)
        self.__社員.append(有限責任社員(間接責任()))

    def 配当(self):
        pass  # 出資割合

    def 納税(self):
        pass  # 法人課税+所得税(二重課税)

    def 組織変更(self, 組織):
        if type(組織) is 合同会社:
            return 組織
        else:
            raise Exception('変更不可')

    def _資本金(self):
        資本金 = 金銭(0)
        for 資本 in self._資本:
            if type(資本) is type(資本金):
                資本金 += 資本
            elif type(資本) is 不動産:
                _金銭 = 資本.価値
                資本金 += _金銭

        if 資本金 < 金銭(1):
            raise Exception('資本金1円以上')
        self._資本金 = 資本金


class 特例有限会社(株式会社):
    def __init__(self, 社員):
        raise Exception('H18有限会社法廃止')


class 合名会社(持分会社):
    def __init__(self, 社員構成):
        if 有限責任社員(間接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')
        if 有限責任社員(直接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')

        [社員.権利.append(業務執行権()) for 社員 in 社員構成]
        [社員.権利.append(会社代表権()) for 社員 in 社員構成]

        self._社員 = 社員構成
        self._法人格 = True

        self._資本 = []
        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        [self._資本.append(社員.出資('信用')) for 社員 in self._社員]
        [self._資本.append(社員.出資('労務')) for 社員 in self._社員]

    def 退社制度(self, 社員):
        self._社員.remove(社員)

    def 持分の譲渡(self, 譲渡する社員):
        承認社員 = self._社員
        承認社員.remove(譲渡する社員)
        for 社員 in 承認社員:
            if not 社員.承認(譲渡する社員):
                raise Exception('持分の譲渡はできない')
            else:
                self._社員.remove(譲渡する社員)


class 合資会社(持分会社):
    def __init__(self, 社員構成):
        if len(社員構成) < 2:
            raise Exception('構成員2名以上')
        if 有限責任社員(直接責任()) not in 社員構成:
            raise Exception('有限責任社員が必要')
        if 無限責任社員(直接責任()) not in 社員構成:
            raise Exception('無限責任社員が必要')

        self._資本 = []
        [社員.権利.append(業務執行権()) for 社員 in 社員構成]

        self._社員 = 社員構成
        self._法人格 = True

        for 社員 in self._社員:
            if type(社員) is type(有限責任社員(直接責任())):
                if 社員.資本['財産'] is None:
                    raise Exception('直接有限責任社員の出資は金銭等に限られる')

        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        [self._資本.append(社員.出資('信用')) for 社員 in self._社員 if type(社員) is type(無限責任社員(直接責任()))]
        [self._資本.append(社員.出資('労務')) for 社員 in self._社員 if type(社員) is type(無限責任社員(直接責任()))]


class 合同会社(持分会社):
    def __init__(self, 社員構成):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        if 無限責任社員(間接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')

        self._資本 = []
        [社員.権利.append(業務執行権()) for 社員 in 社員構成]

        self._社員 = 社員構成
        self._法人格 = True
        self._定款認証 = False
        self._決算公告義務 = False
        self._存続期間 = False

        for 社員 in self._社員:
            if 社員.資本['財産'] is None:
                raise Exception('出資は金銭等に限られる')
        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        self._資本金()

    def 配当(self):
        pass  # 自由

    def 納税(self):
        pass  # 法人課税+所得税(二重課税)

    def 組織変更(self, 組織):
        if type(組織) is 株式会社:
            return 組織
        else:
            raise Exception('変更不可')

    def _資本金(self):
        資本金 = 金銭(0)
        for 資本 in self._資本:
            if type(資本) is type(資本金):
                資本金 += 資本
        if 資本金 < 金銭(1):
            raise Exception('資本金1円以上')


class 有限責任事業組合(持分会社):
    def __init__(self, 社員構成):
        if len(社員構成) < 2:
            raise Exception('構成員2名以上')
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        if 無限責任社員(間接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')

        self._社員 = 社員構成
        self._法人格 = False
        self._定款認証 = False
        self._決算公告義務 = False
        self._存続期間 = True

        self._資本 = []
        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        self._資本金()

    def _資本金(self):
        資本金 = 金銭(0)
        for 資本 in self._資本:
            if type(資本) is type(資本金):
                資本金 += 資本
        if 資本金 < 金銭(2):
            raise Exception('資本金2円以上')
        self._資本金 = 資本金

    def 配当(self):
        pass  # 自由

    def 納税(self):
        pass  # 構成員課税

    def 組織変更(self, 組織):
        raise Exception('変更不可')


class 責任:
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return type(self) != type(other)


class 直接責任(責任):
    pass


class 間接責任(責任):
    pass


class 権利:
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return type(self) != type(other)


class 業務執行権(権利):
    pass


class 会社代表権(権利):
    pass


class 資本:
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return type(self) != type(other)


class 財産(資本):
    pass


class 信用(資本):
    pass


class 労務(資本):
    pass


class 金銭(財産):
    _金額 = 0
    _通貨 = '円'

    @property
    def 金額(self):
        return self._金額

    @property
    def 通貨(self):
        return self._通貨

    def __init__(self, 金額, 通貨=None):
        self._金額 = 金額
        if 通貨 is not None:
            self._通貨 = 通貨

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not self._金額 == other.金額:
            return False
        if not self._通貨 == other.通貨:
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        if not self._金額 == other.金額:
            return True
        if not self._通貨 == other.通貨:
            return True
        return type(self) != type(other)

    def __add__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return 金銭(self._金額 + other.金額, self._通貨)

    def __sub__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return 金銭(self._金額 - other.金額, self._通貨)

    def __mul__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return 金銭(self._金額 * other.金額, self._通貨)

    def __truediv__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return 金銭(self._金額 / other.金額, self._通貨)

    def __lt__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return self._金額 < other.金額

    def __le__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return self._金額 <= other.金額

    def __gt__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return self._金額 > other.金額

    def __ge__(self, other):
        if not self._通貨 == other.通貨:
            raise MoneyException
        return self._金額 >= other.金額


class MoneyException(Exception):
    pass


class 不動産(財産):
    @property
    def 価値(self):
        return self._価値

    def __init__(self, 価値):
        self._価値 = 価値

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not self._価値 == other.価値:
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        if not self._価値 == other.価値:
            return True
        return type(self) != type(other)

    def __add__(self, other):
        return 不動産(self._価値 + other.価値)

    def __sub__(self, other):
        return 不動産(self._価値 - other.価値)

    def __mul__(self, other):
        return 不動産(self._価値 * other.価値)

    def __truediv__(self, other):
        return 不動産(self.価値 / other.価値)

    def __lt__(self, other):
        return self._価値 < other.価値

    def __le__(self, other):
        return self._価値 <= other.価値

    def __gt__(self, other):
        return self._価値 > other.価値

    def __ge__(self, other):
        return self._価値 >= other.価値


class 社員:
    _責任 = 責任()
    _権利 = []
    _資本 = {}

    def __init__(self, 責任, 資本=None,発起人=True):
        if 資本 is None:
            資本 = {'財産': [財産()], '信用': [信用()], '労務': [労務()]}
        self._責任 = 責任
        self._資本 = 資本
        self._発起人 = 発起人

    @property
    def 責任(self):
        return self._責任

    @property
    def 権利(self):
        return self._権利

    @権利.setter
    def 権利(self, 権利):
        self._権利 = 権利

    @property
    def 資本(self):
        return self._資本

    @資本.setter
    def 資本(self, 資本):
        self._資本 = 資本

    @property
    def 発起人(self):
        return self._発起人

    def 出資(self, 資本):
        _資本 = self._資本[資本]
        if self._発起人 == True:
            return _資本
        else:
            if type(_資本) is not 金銭:
                raise Exception('現物出資できるのは発起人に限られる')
            else:
                return _資本

    def 承認(self, 社員):
        return False

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.責任 != other.責任:
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return type(self) != type(other)


class 無限責任社員(社員):
    pass


class 有限責任社員(社員):
    pass


from abc import ABC
from abc import abstractmethod


class 会社設立(ABC):
    def __init__(self, 会社):
        self._会社 = 会社
        self._出資者 = []
        for 出資者 in self._会社.社員:
            if 出資者.発起人 == True:
                self._出資者.append(出資者)

    @abstractmethod
    def 実施(self):
        pass

    def __定款の作成(self):
        pass

    def __出資の履行(self):
        pass

    def __機関の設置(self):
        pass


class 発起設立(会社設立):
    def 実施(self):
        self.__定款の作成()
        self.__出資の履行()
        self.__機関の設置()
        return 株式会社(self._出資者,
                    設立登記=self._設立登記,
                    定款=self._定款
                    )

    def __定款の作成(self):
        print('公証人による定款認証')
        self._定款 = 定款()

    def __出資の履行(self):
        print('出資の払込')

    def __機関の設置(self):
        print('取締役の選任')
        print('検査役の調査等')
        self.__設立登記()

    def __設立登記(self):
        print('設立登記')
        self._設立登記 = '発起人が定めた日から2週間以内'


class 募集設立(会社設立):
    def 実施(self):
        self.__定款の作成()
        self.__出資の履行()
        self.__機関の設置()
        return 株式会社(self._出資者,
                    払込金保管証明=True,
                    創立総会=True,
                    設立登記=self._設立登記,
                    定款=self._定款
                    )

    def __定款の作成(self):
        print('公証人による定款認証')
        self._定款 = 定款()

    def __出資の履行(self):
        self.__株主の募集()
        print('出資の払込')
        print('設立総会')

    def __機関の設置(self):
        print('取締役の選任')
        print('検査役の調査等')
        self.__設立登記()

    def __株主の募集(self):
        print('株主の募集')
        for _出資者 in self._会社.社員:
            if _出資者.発起人 == False:
                self._出資者.append(_出資者)

    def __設立登記(self):
        print('設立登記')
        self._設立登記 = '創立総会の終結の日の翌日から2週間以内'


class 定款():
    def __init__(self):
        self.__絶対的記載事項 = 絶対的記載事項()
        self.__相対的記載事項 = 相対的記載事項()
        self.__任意的記載事項 = 任意的記載事項()

    @property
    def 絶対的記載事項(self):
        return self.__絶対的記載事項

    @property
    def 相対的記載事項(self):
        return self.__相対的記載事項

    @property
    def 任意的記載事項(self):
        return self.__任意的記載事項


class 絶対的記載事項():
    __会社の目的 = '会社の事業目的を記載する'
    __商号 = '会社が自己を表すために用いる名称'
    __本店の所在地 = '最小行政区画（市町村／東京特別区）により記載'
    __設立に際して出資される財産の価格またはその最低額 = 'これに記載された額以上の財産が現実に出資されなければならない'
    __発起人の氏名または名称および住所 = 'これに記載されたものが発起人となる'
    __発行可能株式総数 = '株主総会の決議によらず、取締役会の決議だけで発行することが株式数で、この上限の範囲内であれば、取締役会で自由に株式を発行できる'
    
    @property
    def 会社の目的(self):
        return self.__会社の目的

    @property
    def 商号(self):
        return self.__商号

    @property
    def 本店の所在地(self):
        return self.__本店の所在地

    @property
    def 設立に際して出資される財産の価格またはその最低額(self):
        return self.__設立に際して出資される財産の価格またはその最低額

    @property
    def 発起人の氏名または名称および住所(self):
        return self.__発起人の氏名または名称および住所

    @property
    def 発行可能株式総数(self):
        return self.__発行可能株式総数

class 変態設立事項():
    __現物出資 = '金銭以外の財産をもってする出資'
    __財産引受け = '会社のために会社の成立を条件として特定の財産を譲り受けることを約する契約'
    __発起人の報酬その他の特別の利益 = '設立中の会社の機関として行った労務に対する報酬その他の利益'
    __設立費用 = '会社設立に必要な取引行為から生じる費用のうち、会社が負担すべきもの'
    
    @property
    def 現物出資(self):
        return self.__現物出資

    @property
    def 財産引受け(self):
        return self.__財産引受け

    @property
    def 発起人の報酬その他の特別の利益(self):
        return self.__発起人の報酬その他の特別の利益

    @property
    def 設立費用(self):
        return self.__設立費用

class 相対的記載事項():
    __変態設立事項 = 変態設立事項()

    @property
    def 変態設立事項(self):
        return self.__変態設立事項


class 任意的記載事項():
    pass
