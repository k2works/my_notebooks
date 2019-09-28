from 会社.持分会社 import 持分会社
from 社員.社員 import 有限責任社員
from 社員.責任 import 間接責任
from 社員.責任 import 直接責任
from 権利.権利 import 業務執行権
from 権利.権利 import 会社代表権

class 合名会社(持分会社):
    def __init__(self, 社員構成):
        if 有限責任社員(間接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')
        if 有限責任社員(直接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')

        [社員.権利.append(業務執行権()) for 社員 in 社員構成]
        [社員.権利.append(会社代表権()) for 社員 in 社員構成]

        self._社員 = 社員構成
        self._法人格 = True

        self._資本 = []
        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        [self._資本.append(社員.出資('信用')) for 社員 in self._社員]
        [self._資本.append(社員.出資('労務')) for 社員 in self._社員]

    def 退社制度(self, 社員):
        self._社員.remove(社員)

    def 持分の譲渡(self, 譲渡する社員):
        承認社員 = self._社員
        承認社員.remove(譲渡する社員)
        for 社員 in 承認社員:
            if not 社員.承認(譲渡する社員):
                raise Exception('持分の譲渡はできない')
            else:
                self._社員.remove(譲渡する社員)
