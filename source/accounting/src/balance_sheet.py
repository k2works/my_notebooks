from src.share import 金銭, 科目


class 資産:
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳

    def has内訳(self):
        return True


class 負債:
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳


class 純資産:
    def __init__(self, 内訳):
        self.__内訳 = 内訳

    @property
    def 内訳(self):
        return self.__内訳

    def has内訳(self):
        return True


class 流動資産(資産):
    pass


class 現金及び預金(科目):
    pass


class 受取手形(科目):
    pass


class 売掛金(科目):
    pass


class 貸倒引当金(科目):
    pass


class 有価証券(科目):
    pass


class 商品(科目):
    pass


class 前払費用(科目):
    pass


class 未収収益(科目):
    pass


class 固定資産(資産):
    pass


class 有形固定資産(固定資産):
    pass


class 土地(科目):
    pass


class 建物(科目):
    pass


class 減価償却累計(科目):
    pass


class 無形固定資産(固定資産):
    pass


class のれん(科目):
    pass


class 投資その他の資産(固定資産):
    pass


class 関係会社株式(科目):
    pass


class 投資有価証券(科目):
    pass


class 長期貸付金(科目):
    pass


class 繰延資産(資産):
    pass


class 開業費(科目):
    pass


class 流動負債(負債):
    pass


class 買掛金(科目):
    pass


class 短期借入金(科目):
    pass


class 未払法人税等(科目):
    pass


class 未払費用(科目):
    pass


class 前受収益(科目):
    pass


class 賞与引当金(科目):
    pass


class 固定負債(負債):
    pass


class 社債(科目):
    pass


class 長期借入金(科目):
    pass


class 退職給付金(科目):
    pass


class 株主資本(純資産):
    pass


class 資本金(科目):
    pass


class 資本剰余金(純資産):
    pass


class 資本準備金(科目):
    pass


class その他資本剰余金(科目):
    pass


class 利益剰余金(純資産):
    pass


class 利益準備金(科目):
    pass


class その他利益剰余金(純資産):
    pass


class 任意積立金(科目):
    pass


class 繰越利益剰余金(科目):
    pass


class 自己株式(科目):
    pass


class 評価換算差額等(科目):
    pass


class 新株予約権(科目):
    pass


class 貸借対照表:
    def __init__(self, 流動資産, 固定資産, 繰延資産, 流動負債, 固定負債, 純資産):
        self.__流動資産 = 流動資産
        self.__固定資産 = 固定資産
        self.__繰延資産 = 繰延資産
        self.__流動負債 = 流動負債
        self.__固定負債 = 固定負債
        self.__純資産 = 純資産

    @property
    def 流動資産(self):
        return self.__流動資産

    @property
    def 固定資産(self):
        return self.__固定資産

    @property
    def 繰延資産(self):
        return self.__繰延資産

    @property
    def 流動負債(self):
        return self.__流動負債

    @property
    def 固定負債(self):
        return self.__固定負債

    @property
    def 純資産(self):
        return self.__純資産

    @property
    def 資産合計(self):
        return self.流動資産合計 + self.固定資産合計 + self.繰延資産合計

    @property
    def 負債純資産合計(self):
        return self.流動負債合計 + self.固定負債合計 + self.純資産合計

    @property
    def 流動資産合計(self):
        集計金 = 金銭(0)

        for _科目 in self.__流動資産.内訳:
            集計金 = self.貸方集計金計算(_科目, 集計金)

        return 集計金

    @property
    def 固定資産合計(self):
        集計金 = 金銭(0)

        for _資産 in self.__固定資産.内訳:
            集計金 = self.集計金導出(_資産, 集計金, 科目.貸)

        return 集計金

    @property
    def 繰延資産合計(self):
        集計金 = 金銭(0)

        for _科目 in self.__繰延資産.内訳:
            集計金 = self.集計金計算(_科目, '', 集計金)

        return 集計金

    @property
    def 流動負債合計(self):
        集計金 = 金銭(0)

        for _科目 in self.__流動負債.内訳:
            集計金 = self.集計金計算(_科目, '', 集計金)

        return 集計金

    @property
    def 固定負債合計(self):
        集計金 = 金銭(0)

        for _科目 in self.__固定負債.内訳:
            集計金 = self.集計金計算(_科目, '', 集計金)

        return 集計金

    @property
    def 純資産合計(self):
        集計金 = 金銭(0)

        for _資産 in self.__純資産.内訳:
            集計金 = self.集計金導出(_資産, 集計金, 科目.借)

        return 集計金

    def 集計金導出(self, _資産, 集計金, 貸借):
        if _資産.has内訳():
            for _科目 in _資産.内訳:
                集計金 = self.集計金導出実施(_科目, 貸借, 集計金)
        else:
            return self.借方集計金計算(_資産, 集計金)

        return 集計金

    def 集計金導出実施(self, _科目, 貸借, 集計金):
        if _科目.has内訳():
            return self.集計金導出(_科目, 集計金, 貸借)
        else:
            return self.集計金計算(_科目, 貸借, 集計金)

    def 集計金計算(self, _科目, 貸借, 集計金):
        if 貸借 == 科目.借:
            return self.借方集計金計算(_科目, 集計金)
        elif 貸借 == 科目.貸:
            return self.貸方集計金計算(_科目, 集計金)
        else:
            return 集計金 + _科目.金銭

    def 借方集計金計算(self, _科目, 集計金):
        if _科目.貸借 == _科目.借:
            return 集計金 - _科目.金銭
        else:
            return 集計金 + _科目.金銭

    def 貸方集計金計算(self, _科目, 集計金):
        if _科目.貸借 == 科目.貸:
            return 集計金 - _科目.金銭
        else:
            return 集計金 + _科目.金銭
