class 会社:
    pass


class 人的会社(会社):
    def __str__(self):
        return "所有と経営が一致"


class 物的会社(会社):
    def __str__(self):
        return "所有と経営が分離"
