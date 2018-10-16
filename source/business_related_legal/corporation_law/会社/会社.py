from abc import ABC
from abc import abstractmethod


class 会社:
    pass


class 人的会社(会社):
    def __str__(self):
        return "所有と経営が一致"


class 物的会社(会社):
    def __str__(self):
        return "所有と経営が分離"


class 非公開会社(ABC):
    @abstractmethod
    def is非公開会社(self):
        pass


class 公開会社(ABC):
    @abstractmethod
    def is公開会社(self):
        pass
