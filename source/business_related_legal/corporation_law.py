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
    def __init__(self, 社員構成):
        if 有限責任社員(間接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')
        if 有限責任社員(直接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')
        self._社員 = 社員構成
        self._法人格 = True


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


class 社員:
    def __init__(self, 責任):
        self.__責任 = 責任

    @property
    def 責任(self):
        return self.__責任

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
