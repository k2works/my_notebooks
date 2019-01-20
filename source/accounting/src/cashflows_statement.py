from share import 金銭, 科目


class キャッシュフロー:
    def __init__(self, 金額):
        self.__金銭 = 金銭(金額)

    @property
    def 金銭(self):
        return self.__金銭

    @property
    def 金額(self):
        return self.__金銭.金額

    def has内訳(self):
        return False


class 財務活動によるキャッシュフロー(キャッシュフロー):
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳

    def has内訳(self):
        return True


class 短期借入れによる収入(キャッシュフロー):
    pass


class 短期借入金の返済による支出(キャッシュフロー):
    pass


class 長期借入れによる収入(キャッシュフロー):
    pass


class 長期借入金の返済による支出(キャッシュフロー):
    pass


class 社債の発行による収入(キャッシュフロー):
    pass


class 社債の償還による支出(キャッシュフロー):
    pass


class 株式の発行による収入(キャッシュフロー):
    pass


class 自己株式の取得による支出(キャッシュフロー):
    pass


class 配当金の支払額(キャッシュフロー):
    pass


class 投資活動によるキャッシュフロー(キャッシュフロー):
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳

    def has内訳(self):
        return True


class 有価証券の取得による支出(キャッシュフロー):
    pass


class 有価証券の売却による収入(キャッシュフロー):
    pass


class 有形固定資産の取得による支出(キャッシュフロー):
    pass


class 有形固定資産の売却による収入(キャッシュフロー):
    pass


class 投資有価証券の取得による支出(キャッシュフロー):
    pass


class 投資有価証券の売却による収入(キャッシュフロー):
    pass


class 貸付けによる支出(キャッシュフロー):
    pass


class 貸付金の回収による収入(キャッシュフロー):
    pass


class 営業活動によるキャッシュフロー(キャッシュフロー):
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳

    def has内訳(self):
        return True


class 減価償却費(キャッシュフロー):
    pass


class 税引前当期純利益(キャッシュフロー):
    pass


class 貸倒引当金の増加額(キャッシュフロー):
    pass


class 受取利息および受取配当金(キャッシュフロー):
    pass


class 支払利息(キャッシュフロー):
    pass


class 有形固定資産売却損益(キャッシュフロー):
    pass


class 売上債権の増加額(キャッシュフロー):
    pass


class 棚卸資産の増加額(キャッシュフロー):
    pass


class 仕入債務の増加額(キャッシュフロー):
    pass


class 利息および配当金の受取額(キャッシュフロー):
    pass


class 利息の支払額(キャッシュフロー):
    pass


class 法人税等の支払額(キャッシュフロー):
    pass


class 現金および現金同等物の期首残高(キャッシュフロー):
    pass


class キャッシュフロー計算書:
    def __init__(self, 営業活動によるキャッシュフロー=None, 投資活動によるキャッシュフロー=None, 財務活動によるキャッシュフロー=None, 現金および現金同等物の期首残高=None):
        self.__営業活動によるキャッシュフロー = 営業活動によるキャッシュフロー
        self.__投資活動によるキャッシュフロー = 投資活動によるキャッシュフロー
        self.__財務活動によるキャッシュフロー = 財務活動によるキャッシュフロー
        self.__現金および現金同等物の期首残高 = 現金および現金同等物の期首残高

    @property
    def 営業活動によるキャッシュフロー(self):
        return self.__営業活動によるキャッシュフロー

    @property
    def 投資活動によるキャッシュフロー(self):
        return self.__投資活動によるキャッシュフロー

    @property
    def 財務活動によるキャッシュフロー(self):
        return self.__財務活動によるキャッシュフロー

    @property
    def 営業活動によるキャッシュフロー合計(self):
        return self.キャッシュフロー集計(self.営業活動によるキャッシュフロー.内訳, 金銭(0))

    @property
    def 投資活動によるキャッシュフロー合計(self):
        return self.キャッシュフロー集計(self.投資活動によるキャッシュフロー.内訳, 金銭(0))

    @property
    def 財務活動によるキャッシュフロー合計(self):
        return self.キャッシュフロー集計(self.財務活動によるキャッシュフロー.内訳, 金銭(0))

    @property
    def 現金および現金同等物の期首残高(self):
        return self.__現金および現金同等物の期首残高.金銭

    @property
    def 現金および現金同等物の期末残高(self):
        return self.現金および現金同等物の増加額 + self.現金および現金同等物の期首残高

    @property
    def 現金および現金同等物の増加額(self):
        return self.営業活動によるキャッシュフロー合計 + self.投資活動によるキャッシュフロー合計 + self.財務活動によるキャッシュフロー合計

    def キャッシュフロー集計(self, 内訳, 集計金):
        for _キャッシュフロー in 内訳:
            集計金 += 金銭(_キャッシュフロー.金額)

        return 集計金
