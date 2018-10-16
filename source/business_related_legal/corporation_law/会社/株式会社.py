from 会社.会社 import 物的会社
from 社員.社員 import 無限責任社員
from 社員.責任 import 直接責任
from 社員.責任 import 間接責任
from 資本.資本 import 金銭
from 資本.資本 import 不動産
from 会社.合同会社 import 合同会社

from 会社.会社 import 非公開会社, 公開会社
from 資本.種類株式 import 議決権制限株式


class 株式会社(物的会社, 非公開会社, 公開会社):
    _社員 = []
    _資本 = []

    def __init__(self, 社員構成, 払込金保管証明=False, 創立総会=False, 設立登記=None, 定款=None):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')

        self._社員 = 社員構成
        self._法人格 = True
        self._定款認証 = True
        self._決算公告義務 = True
        self._存続期間 = False
        self._払込金保管証明 = 払込金保管証明
        self._創立総会 = 創立総会
        self._設立登記 = 設立登記
        self._定款 = 定款

        self._資本 = []

        for 社員 in self._社員:
            _出資 = 社員.出資('財産')
            if type(_出資) is list:
                for 資本 in _出資:
                    self._資本.append(資本)
            else:
                self._資本.append(_出資)
        self._資本金()

    @property
    def 社員(self):
        return self._社員

    @property
    def 法人格(self):
        return self._法人格

    @property
    def 資本(self):
        return self._資本

    @property
    def 払込金保管証明(self):
        return self._払込金保管証明

    @property
    def 創立総会(self):
        return self._創立総会

    @property
    def 設立登記(self):
        return self._設立登記

    @property
    def 定款(self):
        return self._定款

    def 退社制度(self, 社員):
        raise Exception('退社制度は認められない')

    def 株式の譲渡(self, 譲渡する社員):
        self.__社員.remove(譲渡する社員)
        self.__社員.append(有限責任社員(間接責任()))

    def 配当(self):
        pass  # 出資割合

    def 納税(self):
        pass  # 法人課税+所得税(二重課税)

    def 組織変更(self, 組織):
        if type(組織) is 合同会社:
            return 組織
        else:
            raise Exception('変更不可')

    def _資本金(self):
        資本金 = 金銭(0)
        for 資本 in self._資本:
            if type(資本) is type(資本金):
                資本金 += 資本
            elif type(資本) is 不動産:
                _金銭 = 資本.価値
                資本金 += _金銭

        if 資本金 < 金銭(1):
            raise Exception('資本金1円以上')
        self._資本金 = 資本金

    def is非公開会社(self):
        複数種類株式 = []
        check = False

        for 社員 in self.社員:
            [複数種類株式.append(株式) for 株式 in 社員.株式]
            for 株式 in 複数種類株式:
                check = True if type(株式) is 議決権制限株式 else False

        return check

    def is公開会社(self):
        複数種類株式 = []

        for 社員 in self.社員:
            [複数種類株式.append(株式) for 株式 in 社員.株式]
            for 株式 in 複数種類株式:
                if type(株式) is not 議決権制限株式:
                    return True


class 特例有限会社(株式会社):
    def __init__(self, 社員):
        raise Exception('H18有限会社法廃止')
