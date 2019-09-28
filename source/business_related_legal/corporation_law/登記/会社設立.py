from abc import ABC
from abc import abstractmethod


class 会社設立(ABC):
    def __init__(self, 会社):
        self._会社 = 会社
        self._出資者 = []
        for 出資者 in self._会社.社員:
            if 出資者.発起人 == True:
                self._出資者.append(出資者)

    @abstractmethod
    def 実施(self):
        pass

    def __定款の作成(self):
        pass

    def __出資の履行(self):
        pass

    def __機関の設置(self):
        pass
