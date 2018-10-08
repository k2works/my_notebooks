from 会社.持分会社 import 持分会社
from 社員.社員 import 無限責任社員
from 社員.責任 import 直接責任
from 社員.責任 import 間接責任
from 資本.資本 import 金銭


class 有限責任事業組合(持分会社):
    def __init__(self, 社員構成):
        if len(社員構成) < 2:
            raise Exception('構成員2名以上')
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        if 無限責任社員(間接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')

        self._社員 = 社員構成
        self._法人格 = False
        self._定款認証 = False
        self._決算公告義務 = False
        self._存続期間 = True

        self._資本 = []
        [self._資本.append(社員.出資('財産')) for 社員 in self._社員]
        self._資本金()

    def _資本金(self):
        資本金 = 金銭(0)
        for 資本 in self._資本:
            if type(資本) is type(資本金):
                資本金 += 資本
        if 資本金 < 金銭(2):
            raise Exception('資本金2円以上')
        self._資本金 = 資本金

    def 配当(self):
        pass  # 自由

    def 納税(self):
        pass  # 構成員課税

    def 組織変更(self, 組織):
        raise Exception('変更不可')
