from 会社.持分会社 import 持分会社
from 社員.社員 import 有限責任社員
from 社員.社員 import 無限責任社員
from 社員.責任 import 直接責任
from 権利.権利 import 業務執行権


class 合資会社(持分会社):
    def __init__(self, 社員構成):
        if len(社員構成) < 2:
            raise Exception('構成員2名以上')
        if 有限責任社員(直接責任()) not in 社員構成:
            raise Exception('有限責任社員が必要')
        if 無限責任社員(直接責任()) not in 社員構成:
            raise Exception('無限責任社員が必要')

        self._資本 = []
        [社員.権利.append(業務執行権()) for 社員 in 社員構成]

        self._社員 = 社員構成
        self._法人格 = True

        for 社員 in self._社員:
            if type(社員) is type(有限責任社員(直接責任())):
                if 社員.資本['財産'] is None:
                    raise Exception('直接有限責任社員の出資は金銭等に限られる')

        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        [self._資本.append(社員.出資('信用')) for 社員 in self._社員 if type(社員) is type(無限責任社員(直接責任()))]
        [self._資本.append(社員.出資('労務')) for 社員 in self._社員 if type(社員) is type(無限責任社員(直接責任()))]
