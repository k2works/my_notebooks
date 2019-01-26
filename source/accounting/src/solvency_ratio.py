import math
from src.balance_sheet import *


class 安全性分析:
    def __init__(self, 貸借対照表=None):
        self.__貸借対照表 = 貸借対照表

    @property
    def 流動比率(self):
        _流動比率 = (self.__貸借対照表.流動資産合計.金額 / self.__貸借対照表.流動負債合計.金額) * 100
        return math.ceil(_流動比率)

    @property
    def 当座比率(self):
        _流動資産 = self.__貸借対照表.流動資産.内訳
        _当座資産 = 0
        for item in _流動資産:
            if type(item) in [現金及び預金, 売掛金, 有価証券]:
                _当座資産 += item.金額
            if type(item) in [貸倒引当金]:
                _当座資産 -= item.金額
        _当座比率 = (_当座資産 / self.__貸借対照表.流動負債合計.金額) * 100
        return math.ceil(_当座比率)

    @property
    def 固定比率(self):
        _自己資本 = self.__自己資本()
        _固定比率 = (self.__貸借対照表.固定資産合計.金額 / _自己資本) * 100
        return math.ceil(_固定比率)

    @property
    def 固定長期適合率(self):
        _固定長期適合率 = 0
        _固定資産 = self.__貸借対照表.固定資産合計.金額
        _自己資本 = self.__自己資本()
        _固定負債 = self.__貸借対照表.固定負債合計.金額
        _固定長期適合率 = _固定資産 / (_固定負債 + _自己資本)
        return math.ceil(_固定長期適合率)

    @property
    def 自己資本比率(self):
        _自己資本比率 = 0
        _自己資本 = self.__自己資本()
        _総資本 = self.__貸借対照表.固定負債合計.金額 + self.__貸借対照表.流動負債合計.金額 + self.__貸借対照表.純資産合計.金額
        _自己資本比率 = (_自己資本 / _総資本) * 100
        return math.ceil(_自己資本比率)

    @property
    def 負債比率(self):
        _負債比率 = 0
        _負債 = self.__貸借対照表.固定負債合計.金額 + self.__貸借対照表.流動負債合計.金額
        _自己資本 = self.__自己資本()
        _負債比率 = (_負債 / _自己資本) * 100
        return math.ceil(_負債比率)

    def __自己資本(self):
        _自己資本 = self.__貸借対照表.純資産合計.金額
        for item in self.__貸借対照表.純資産.内訳:
            if type(item) in [新株予約権]:
                _自己資本 -= item.金額
        return _自己資本
