from share import 金銭


class 科目:
    def __init__(self, 金額):
        self.__金銭 = 金銭(金額)

    @property
    def 金額(self):
        return self.__金銭.金額


class 売上高(科目):
    pass


class 売上原価(科目):
    pass


class 売上総利益(科目):
    pass


class 販管費(科目):
    pass


class 営業利益(科目):
    pass


class 営業外収益(科目):
    pass


class 営業外費用(科目):
    pass


class 経常利益(科目):
    pass


class 特別利益(科目):
    pass


class 特別損失(科目):
    pass


class 税引前当期純利益(科目):
    pass


class 法人税等(科目):
    法人税率 = 0.4

    def __init__(self, 金額):
        self.__金銭 = 金銭(金額)

    @property
    def 金額(self):
        return self.__金銭.金額 * self.法人税率


class 当期純利益(科目):
    pass


class 損益計算書:
    def __init__(self, 売上高=売上高(0), 売上原価=売上原価(0), 販管費=販管費(0), 営業外収益=営業外収益(0), 営業外費用=営業外費用(0), 特別利益=特別利益(0),
                 特別損失=特別損失(0)):
        self.__売上高 = 売上高
        self.__売上原価 = 売上原価
        self.__販管費 = 販管費
        self.__営業外収益 = 営業外収益
        self.__営業外費用 = 営業外費用
        self.__特別利益 = 特別利益
        self.__特別損失 = 特別損失

    @property
    def 売上高(self):
        return self.__売上高

    @property
    def 売上原価(self):
        return self.__売上原価

    @property
    def 売上総利益(self):
        return 売上総利益(self.__売上高.金額 - self.__売上原価.金額)

    @property
    def 販管費(self):
        return self.__販管費

    @property
    def 営業利益(self):
        return 営業利益(self.売上総利益.金額 - self.__販管費.金額)

    @property
    def 営業外収益(self):
        return self.__営業外収益

    @property
    def 営業外費用(self):
        return self.__営業外費用

    @property
    def 経常利益(self):
        return 経常利益(self.営業利益.金額 + self.__営業外収益.金額 - self.__営業外費用.金額)

    @property
    def 特別利益(self):
        return self.__特別利益

    @property
    def 特別損失(self):
        return self.__特別損失

    @property
    def 税引前当期純利益(self):
        return 税引前当期純利益(self.経常利益.金額 + self.__特別利益.金額 - self.__特別損失.金額)

    @property
    def 法人税等(self):
        return 法人税等(self.税引前当期純利益.金額)

    @property
    def 当期純利益(self):
        return 当期純利益(self.税引前当期純利益.金額 - self.法人税等.金額)
