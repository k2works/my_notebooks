import math
from src.balance_sheet import *

class 比率:
    def __init__(self, 値, 単位='%'):
        self.__値 = 値
        self.__単位 = 単位

    def __str__(self):
        return f"{self.__値}{self.__単位}"

    @property
    def 値(self):
        return self.__値

    @property
    def 単位(self):
        return self.__単位

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not self.__値 == other.値:
            return False
        if not self.__単位 == other.__単位:
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        if not self.__値 == other.値:
            return True
        if not self.__単位 == other.__単位:
            return True
        return type(self) != type(other)

class 流動比率:
    def __init__(self, 貸借対照表, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _値 = (self.__貸借対照表.流動資産合計.金額 / self.__貸借対照表.流動負債合計.金額) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 当座比率:
    def __init__(self, 貸借対照表, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _流動資産 = self.__貸借対照表.流動資産.内訳
        _当座資産 = 0
        for item in _流動資産:
            if type(item) not in [商品, 貸倒引当金]:
                _当座資産 += item.金額
            if type(item) in [貸倒引当金]:
                _当座資産 -= item.金額
        _値 = (_当座資産 / self.__貸借対照表.流動負債合計.金額) * 100

        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 固定比率:
    def __init__(self, 貸借対照表, 自己資本, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__自己資本 = 自己資本
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _値 = (self.__貸借対照表.固定資産合計.金額 / self.__自己資本) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 固定長期適合率:
    def __init__(self, 貸借対照表, 自己資本, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__自己資本 = 自己資本
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _固定資産 = self.__貸借対照表.固定資産合計.金額
        _自己資本 = self.__自己資本
        _固定負債 = self.__貸借対照表.固定負債合計.金額
        _値 = _固定資産 / (_固定負債 + _自己資本) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 自己資本比率:
    def __init__(self, 貸借対照表, 自己資本, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__自己資本 = 自己資本
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _自己資本 = self.__自己資本
        _総資本 = self.__貸借対照表.固定負債合計.金額 + self.__貸借対照表.流動負債合計.金額 + self.__貸借対照表.純資産合計.金額
        _値 = (_自己資本 / _総資本) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 負債比率:
    def __init__(self, 貸借対照表, 自己資本, 端数処理):
        self.__貸借対照表 = 貸借対照表
        self.__自己資本 = 自己資本
        self.__端数処理 = 端数処理

    @property
    def 値(self):
        _負債 = self.__貸借対照表.固定負債合計.金額 + self.__貸借対照表.流動負債合計.金額
        _自己資本 = self.__自己資本
        _値 = (_負債 / _自己資本) * 100
        self.__値 = 比率(round(_値,self.__端数処理))
        return self.__値

    def __str__(self):
        return str(self.値)

class 安全性分析:
    def __init__(self, 貸借対照表=None):
        self.__貸借対照表 = 貸借対照表

    @property
    def 流動比率(self):
        return 流動比率(self.__貸借対照表, 端数処理=2)

    @property
    def 当座比率(self):
        return 当座比率(self.__貸借対照表, 端数処理=2)

    @property
    def 固定比率(self):
        return 固定比率(self.__貸借対照表, self.__自己資本(), 端数処理=2)

    @property
    def 固定長期適合率(self):
        return 固定長期適合率(self.__貸借対照表, self.__自己資本(), 端数処理=2)

    @property
    def 自己資本比率(self):
        return 自己資本比率(self.__貸借対照表, self.__自己資本(), 端数処理=2)

    @property
    def 負債比率(self):
        return 負債比率(self.__貸借対照表, self.__自己資本(), 端数処理=2)

    def __自己資本(self):
        _自己資本 = self.__貸借対照表.純資産合計.金額
        for item in self.__貸借対照表.純資産.内訳:
            if type(item) in [新株予約権]:
                _自己資本 -= item.金額
        return _自己資本
