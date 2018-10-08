from 会社.持分会社 import 持分会社
from 会社.株式会社 import 株式会社
from 社員.社員 import 無限責任社員
from 社員.責任 import 間接責任
from 社員.責任 import 直接責任
from 権利.権利 import 業務執行権
from 資本.資本 import 金銭


class 合同会社(持分会社):
    def __init__(self, 社員構成):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        if 無限責任社員(間接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')

        self._資本 = []
        [社員.権利.append(業務執行権()) for 社員 in 社員構成]

        self._社員 = 社員構成
        self._法人格 = True
        self._定款認証 = False
        self._決算公告義務 = False
        self._存続期間 = False

        for 社員 in self._社員:
            if 社員.資本['財産'] is None:
                raise Exception('出資は金銭等に限られる')
        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        self._資本金()

    def 配当(self):
        pass  # 自由

    def 納税(self):
        pass  # 法人課税+所得税(二重課税)

    def 組織変更(self, 組織):
        if type(組織) is 株式会社:
            return 組織
        else:
            raise Exception('変更不可')

    def _資本金(self):
        資本金 = 金銭(0)
        for 資本 in self._資本:
            if type(資本) is type(資本金):
                資本金 += 資本
        if 資本金 < 金銭(1):
            raise Exception('資本金1円以上')
