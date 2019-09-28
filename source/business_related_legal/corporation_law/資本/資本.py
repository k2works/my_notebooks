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
