from 登記.会社設立 import 会社設立
from 登記.定款 import 定款
from 会社.株式会社 import 株式会社
from 資本.資本 import 金銭


class 発起設立(会社設立):
    def 実施(self, 種類株式=None):
        self.__定款の作成()
        self.__出資の履行(種類株式)
        self.__機関の設置()
        return 株式会社(self._出資者,
                    設立登記=self._設立登記,
                    定款=self._定款
                    )

    def __定款の作成(self):
        self._定款 = 定款()
        self.__公証人による定款認証()

    def __出資の履行(self, 種類株式):
        self.__出資の払込(種類株式)

    def __機関の設置(self):
        self.__取締役の選任()
        self.__検査役の調査等()
        self.__設立登記()

    def __公証人による定款認証(self):
        pass

    def __出資の払込(self, 種類株式):
        for 出資者 in self._出資者:
            if 種類株式 is not None:
                出資 = 出資者.資本['財産']
                if type(出資) == 金銭:
                    出資者.株式 = 種類株式(出資.金額)

    def __取締役の選任(self):
        pass

    def __検査役の調査等(self):
        pass

    def __設立登記(self):
        self._設立登記 = '発起人が定めた日から2週間以内'
