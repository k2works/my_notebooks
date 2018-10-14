class 自益権:
    pass


class 単独株主権:
    pass


class 少数株主権:
    pass


class 共益権:
    __単独株主権 = 単独株主権()
    __少数株主権 = 少数株主権()

    @property
    def 単独株主権(self):
        return self.__単独株主権

    @property
    def 少数株主権(self):
        return self.__少数株主権


class 株式:
    __単位 = '株'
    __自益権 = 自益権()
    __共益権 = 共益権()

    def __init__(self, 数量):
        self.__数量 = 数量

    def __str__(self):
        return str(self.__数量) + self.__単位

    @property
    def 数量(self):
        return self.__数量

    @property
    def 単位(self):
        return self.__単位

    @property
    def 自益権(self):
        return self.__自益権

    @property
    def 共益権(self):
        return self.__共益権