from 会社.人的会社 import 人的会社

class 持分会社(人的会社):
    _社員 = []
    _資本 = []

    def __init__(self, 社員構成):
        self._社員 = 社員構成
        self._法人格 = True

    @property
    def 社員(self):
        return self._社員

    @property
    def 法人格(self):
        return self._法人格

    @property
    def 資本(self):
        return self._資本

    def 権利義務の帰属主体(self):
        return self._法人格


