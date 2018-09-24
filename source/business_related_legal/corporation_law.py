class 会社:
    pass


class 物的会社(会社):
    def __str__(self):
        return "所有と経営が分離"


class 人的会社(会社):
    def __str__(self):
        return "所有と経営が一致"


class 持分会社(人的会社):
    def __init__(self, 社員構成):
        self._社員 = 社員構成
        self._法人格 = True

    @property
    def 社員(self):
        return self._社員

    @property
    def 法人格(self):
        return self._法人格

    def 権利義務の帰属主体(self):
        return self._法人格


class 株式会社(物的会社):
    def __init__(self, 社員構成):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        self.__社員 = 社員構成
        self.__法人格 = True

    @property
    def 社員(self):
        return self.__社員

    @property
    def 法人格(self):
        return self.__法人格


class 合名会社(持分会社):
    _社員 = []
    _資本 = []

    def __init__(self, 社員構成):
        if 有限責任社員(間接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')
        if 有限責任社員(直接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')

        [社員.権利.append(業務執行権()) for 社員 in 社員構成]
        [社員.権利.append(会社代表権()) for 社員 in 社員構成]

        self._社員 = 社員構成
        self._法人格 = True

        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        [self._資本.append(社員.出資('信用')) for 社員 in self._社員]
        [self._資本.append(社員.出資('労務')) for 社員 in self._社員]

    @property
    def 資本(self):
        return self._資本

    def 退社(self, 社員):
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
        if 有限責任社員(直接責任()) not in 社員構成:
            raise Exception('有限責任社員が必要')
        if 無限責任社員(直接責任()) not in 社員構成:
            raise Exception('無限責任社員が必要')
        self._社員 = 社員構成
        self._法人格 = True


class 合同会社(持分会社):
    def __init__(self, 社員構成):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        if 無限責任社員(間接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        self._社員 = 社員構成
        self._法人格 = True


class 特例有限会社(株式会社):
    def __init__(self, 社員):
        raise Exception('H18有限会社法廃止')


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
