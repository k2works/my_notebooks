from src.share import 比率
from src.balance_sheet import *

class 総資本経常利益率:
    def __init__(self, 貸借対照表, 損益計算書, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__損益計算書 = 損益計算書
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _総資本 = self.__貸借対照表.流動負債合計 + self.__貸借対照表.固定負債合計 + self.__貸借対照表.純資産合計
        _経常利益 = self.__損益計算書.経常利益
        _値 =  (_経常利益.金額 / _総資本.金額) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 総資本当期純利益率:
    def __init__(self, 貸借対照表, 損益計算書, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__損益計算書 = 損益計算書
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _総資本 = self.__貸借対照表.流動負債合計 + self.__貸借対照表.固定負債合計 + self.__貸借対照表.純資産合計
        _当期純利益 = self.__損益計算書.当期純利益
        _値 =  (_当期純利益.金額 / _総資本.金額) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 自己資本当期純利益率:
    def __init__(self, 貸借対照表, 自己資本, 損益計算書, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__自己資本 = 自己資本
        self.__損益計算書 = 損益計算書
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _自己資本 = self.__自己資本
        _当期純利益 = self.__損益計算書.当期純利益
        _値 =  (_当期純利益.金額 / _自己資本.金額) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 総合収益性分析:
    def __init__(self, 貸借対照表=None, 損益計算書=None):
        self.__貸借対照表 = 貸借対照表
        self.__損益計算書 = 損益計算書

    @property
    def 総資本経常利益率(self):
        return 総資本経常利益率(self.__貸借対照表, self.__損益計算書, 端数処理=2)

    @property
    def 総資本当期純利益率(self):
        return 総資本当期純利益率(self.__貸借対照表, self.__損益計算書, 端数処理=2)

    @property
    def 自己資本当期純利益率(self):
        return 自己資本当期純利益率(self.__貸借対照表, self.__自己資本(), self.__損益計算書, 端数処理=2)

    def __自己資本(self):
        _自己資本 = self.__貸借対照表.純資産合計.金額
        for item in self.__貸借対照表.純資産.内訳:
            if type(item) in [新株予約権]:
                _自己資本 -= item.金額
        return 金銭(_自己資本)

class 収益性分析:
    def __init__(self, 損益計算書=None):
        self.__損益計算書 = 損益計算書

    @property
    def 売上高経常利益率(self):
        pass

    @property
    def 売上高営業利益率(self):
        pass

    @property
    def 売上高総利益率(self):
        pass

    @property
    def 売上高販売費一般管理費率(self):
        pass
