from share import 金銭, 科目


class 収益:
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳


class 費用:
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳


class 売上高(科目):
    pass


class 売上原価(科目):
    pass


class 売上総利益(科目):
    pass


class 販管費(費用):
    pass


class 給料賃金(科目):
    pass


class 福利厚生費(科目):
    pass


class 広告宣伝費(科目):
    pass


class 水道光熱費(科目):
    pass


class 交際費(科目):
    pass


class 保険料(科目):
    pass


class 支払家賃(科目):
    pass


class 減価償却費(科目):
    pass


class 営業利益(科目):
    pass


class 営業外収益(収益):
    pass


class 受取利息(科目):
    pass


class 受取配当金(科目):
    pass


class 有価証券評価益(科目):
    pass


class 有価証券売却益(科目):
    pass


class 受取家賃(科目):
    pass


class 仕入割引(科目):
    pass


class 営業外費用(費用):
    pass


class 支払利息(科目):
    pass


class 手形売却損(科目):
    pass


class 有価証券評価損(科目):
    pass


class 有価証券売却損(科目):
    pass


class 売上割引(科目):
    pass


class 経常利益(科目):
    pass


class 特別利益(収益):
    pass


class 固定資産売却益(科目):
    pass


class 国庫補助金受贈益(科目):
    pass


class 特別損失(費用):
    pass


class 固定資産売却損(科目):
    pass


class 災害損失(科目):
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
    def __init__(self, 売上高=売上高(0), 売上原価=売上原価(0), 販管費=販管費(0), 営業外収益=営業外収益(0), 営業外費用=営業外費用(0), 特別利益=特別利益(0), 特別損失=特別損失(0)):
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
    def 販管費合計(self):
        return self.合計計算(self.__販管費.内訳)

    @property
    def 営業利益(self):
        return 営業利益(self.売上総利益.金額 - self.販管費合計.金額)

    @property
    def 営業外収益(self):
        return self.__営業外収益

    @property
    def 営業外収益合計(self):
        return self.合計計算(self.__営業外収益.内訳)

    @property
    def 営業外費用(self):
        return self.__営業外費用

    @property
    def 営業外費用合計(self):
        return self.合計計算(self.__営業外費用.内訳)

    @property
    def 経常利益(self):
        return 経常利益(self.営業利益.金額 + self.営業外収益合計.金額 - self.営業外費用合計.金額)

    @property
    def 特別利益(self):
        return self.__特別利益

    @property
    def 特別利益合計(self):
        return self.合計計算(self.__特別利益.内訳)

    @property
    def 特別損失(self):
        return self.__特別損失

    @property
    def 特別損失合計(self):
        return self.合計計算(self.__特別損失.内訳)

    @property
    def 税引前当期純利益(self):
        return 税引前当期純利益(self.経常利益.金額 + self.特別利益合計.金額 - self.特別損失合計.金額)

    @property
    def 法人税等(self):
        return 法人税等(self.税引前当期純利益.金額)

    @property
    def 当期純利益(self):
        return 当期純利益(self.税引前当期純利益.金額 - self.法人税等.金額)

    def 合計計算(self, 内訳):
        集計金 = 金銭(0)
        for _科目 in 内訳:
            if _科目.貸借 == 科目.借:
                集計金 = 集計金 - _科目.金銭
            else:
                集計金 = 集計金 + _科目.金銭
        return 集計金

