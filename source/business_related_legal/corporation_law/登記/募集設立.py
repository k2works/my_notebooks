from 登記.会社設立 import 会社設立
from 会社.株式会社 import 株式会社
from 登記.定款 import 定款


class 募集設立(会社設立):
    def 実施(self):
        self.__定款の作成()
        self.__出資の履行()
        self.__機関の設置()
        return 株式会社(self._出資者,
                    払込金保管証明=True,
                    創立総会=True,
                    設立登記=self._設立登記,
                    定款=self._定款
                    )

    def __定款の作成(self):
        self._定款 = 定款()
        self.__公証人による定款認証()

    def __出資の履行(self):
        self.__株主の募集()
        self.__出資の払込()
        self.__設立総会()

    def __機関の設置(self):
        self.__取締役の選任()
        self.__設立登記()

    def __公証人による定款認証(self):
        pass

    def __株主の募集(self):
        for _出資者 in self._会社.社員:
            if _出資者.発起人 == False:
                self._出資者.append(_出資者)

    def __出資の払込(self):
        pass

    def __設立総会(self):
        pass

    def __取締役の選任(self):
        pass

    def __検査役の調査等(self):
        pass

    def __設立登記(self):
        self._設立登記 = '創立総会の終結の日の翌日から2週間以内'
