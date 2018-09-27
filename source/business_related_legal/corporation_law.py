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

    def __init__(self, 社員構成):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')

        self._社員 = 社員構成
        self._法人格 = True
        self._定款認証 = True
        self._決算公告義務 = True
        self._存続期間 = False

        self._資本 = []
        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
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


class 社員:
    _責任 = 責任()
    _権利 = []
    _資本 = {}

    def __init__(self, 責任, 資本=None):
        if 資本 is None:
            資本 = {'財産': 財産(), '信用': 信用(), '労務': 労務()}
        self._責任 = 責任
        self._資本 = 資本

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

    def 出資(self, 資本):
        出資 = self._資本[資本]
        del self._資本[資本]
        return 出資

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
