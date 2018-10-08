class 定款():
    def __init__(self):
        self.__絶対的記載事項 = 絶対的記載事項()
        self.__相対的記載事項 = 相対的記載事項()
        self.__任意的記載事項 = 任意的記載事項()

    @property
    def 絶対的記載事項(self):
        return self.__絶対的記載事項

    @property
    def 相対的記載事項(self):
        return self.__相対的記載事項

    @property
    def 任意的記載事項(self):
        return self.__任意的記載事項


class 絶対的記載事項():
    __会社の目的 = '会社の事業目的を記載する'
    __商号 = '会社が自己を表すために用いる名称'
    __本店の所在地 = '最小行政区画（市町村／東京特別区）により記載'
    __設立に際して出資される財産の価格またはその最低額 = 'これに記載された額以上の財産が現実に出資されなければならない'
    __発起人の氏名または名称および住所 = 'これに記載されたものが発起人となる'
    __発行可能株式総数 = '株主総会の決議によらず、取締役会の決議だけで発行することが株式数で、この上限の範囲内であれば、取締役会で自由に株式を発行できる'

    @property
    def 会社の目的(self):
        return self.__会社の目的

    @property
    def 商号(self):
        return self.__商号

    @property
    def 本店の所在地(self):
        return self.__本店の所在地

    @property
    def 設立に際して出資される財産の価格またはその最低額(self):
        return self.__設立に際して出資される財産の価格またはその最低額

    @property
    def 発起人の氏名または名称および住所(self):
        return self.__発起人の氏名または名称および住所

    @property
    def 発行可能株式総数(self):
        return self.__発行可能株式総数


class 変態設立事項():
    __現物出資 = '金銭以外の財産をもってする出資'
    __財産引受け = '会社のために会社の成立を条件として特定の財産を譲り受けることを約する契約'
    __発起人の報酬その他の特別の利益 = '設立中の会社の機関として行った労務に対する報酬その他の利益'
    __設立費用 = '会社設立に必要な取引行為から生じる費用のうち、会社が負担すべきもの'

    @property
    def 現物出資(self):
        return self.__現物出資

    @property
    def 財産引受け(self):
        return self.__財産引受け

    @property
    def 発起人の報酬その他の特別の利益(self):
        return self.__発起人の報酬その他の特別の利益

    @property
    def 設立費用(self):
        return self.__設立費用


class 相対的記載事項():
    __変態設立事項 = 変態設立事項()

    @property
    def 変態設立事項(self):
        return self.__変態設立事項


class 任意的記載事項():
    pass
