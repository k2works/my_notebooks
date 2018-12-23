class 金銭:
    def __init__(self, 金額, 通貨='円'):
        self.__金額 = 金額
        self.__通貨 = 通貨

    def __str__(self):
        return f"{self.__金額} {self.__通貨}"

    @property
    def 金額(self):
        return self.__金額

    @property
    def 通貨(self):
        return self.__通貨

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not self.__金額 == other.金額:
            return False
        if not self.__通貨 == other.通貨:
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        if not self.__金額 == other.金額:
            return True
        if not self.__通貨 == other.通貨:
            return True
        return type(self) != type(other)

    def __add__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return 金銭(self.__金額 + other.金額, self.__通貨)

    def __sub__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return 金銭(self.__金額 - other.金額, self.__通貨)

    def __mul__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return 金銭(self.__金額 * other.金額, self.__通貨)

    def __truediv__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return 金銭(self.__金額 / other.金額, self.__通貨)

    def __lt__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return self.__金額 < other.金額

    def __le__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return self.__金額 <= other.金額

    def __gt__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return self.__金額 > other.金額

    def __ge__(self, other):
        if not self.__通貨 == other.通貨:
            raise MoneyException
        return self.__金額 >= other.金額


class MoneyException(Exception):
    pass


class 科目:
    貸 = '貸方'
    借 = '借方'

    def __init__(self, 金額, 貸方借方=None):
        self.__金銭 = 金銭(金額)
        self.__貸方借方 = 貸方借方

    @property
    def 金銭(self):
        return self.__金銭

    @property
    def 金額(self):
        return self.__金銭.金額

    @property
    def 貸借(self):
        return self.__貸方借方

    def has内訳(self):
        return False
