from 社員.責任 import 責任
from 資本.資本 import 財産
from 資本.資本 import 信用
from 資本.資本 import 労務
from 資本.資本 import 金銭


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

