from 登記.会社設立 import 会社設立
from 登記.定款 import 定款
from 会社.株式会社 import 株式会社


class 発起設立(会社設立):
    def 実施(self):
        self.__定款の作成()
        self.__出資の履行()
        self.__機関の設置()
        return 株式会社(self._出資者,
                    設立登記=self._設立登記,
                    定款=self._定款
                    )

    def __定款の作成(self):
        self._定款 = 定款()
        self.__公証人による定款認証()

    def __出資の履行(self):
        self.__出資の払込()

    def __機関の設置(self):
        self.__取締役の選任()
        self.__検査役の調査等()
        self.__設立登記()

    def __公証人による定款認証(self):
        pass

    def __出資の払込(self):
        pass

    def __取締役の選任(self):
        pass

    def __検査役の調査等(self):
        pass

    def __設立登記(self):
        self._設立登記 = '発起人が定めた日から2週間以内'
