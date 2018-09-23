import unittest


class 会社:
    pass


class 物的会社(会社):
    def __str__(self):
        return "所有と経営が分離"


class 人的会社(会社):
    def __str__(self):
        return "所有と経営が一致"


class 持分会社(人的会社):
    @property
    def 社員(self):
        return self._社員

    @property
    def 法人格(self):
        return self._法人格


class 株式会社(物的会社):
    def __init__(self, 社員構成):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        self.__社員 = 社員構成
        self.__法人格 = True

    @property
    def 社員(self):
        return self.__社員

    @property
    def 法人格(self):
        return self.__法人格


class 合名会社(持分会社):
    def __init__(self, 社員構成):
        if 有限責任社員(間接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')
        if 有限責任社員(直接責任()) in 社員構成:
            raise Exception('無限責任社員のみ')
        self._社員 = 社員構成
        self._法人格 = True


class 合資会社(持分会社):
    def __init__(self, 社員構成):
        if 有限責任社員(直接責任()) not in 社員構成:
            raise Exception('有限責任社員が必要')
        if 無限責任社員(直接責任()) not in 社員構成:
            raise Exception('無限責任社員が必要')
        self._社員 = 社員構成
        self._法人格 = True


class 合同会社(持分会社):
    def __init__(self, 社員構成):
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        if 無限責任社員(間接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        self._社員 = 社員構成
        self._法人格 = True


class 特例有限会社(株式会社):
    def __init__(self, 社員):
        raise Exception('H18有限会社法廃止')


class 有限責任事業組合(持分会社):
    def __init__(self, 社員構成):
        if len(社員構成) < 2:
            raise Exception('構成員2名以上')
        if 無限責任社員(直接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        if 無限責任社員(間接責任()) in 社員構成:
            raise Exception('有限責任社員のみ')
        self._社員 = 社員構成
        self._法人格 = False


class 社員:
    def __init__(self, 責任):
        self.__責任 = 責任

    @property
    def 責任(self):
        return self.__責任

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.責任 != other.責任:
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return type(self) != type(other)


class 無限責任社員(社員):
    pass


class 有限責任社員(社員):
    pass


class 責任:
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return type(self) == type(other)

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return type(self) != type(other)


class 直接責任(責任):
    pass


class 間接責任(責任):
    pass


class 会社テスト(unittest.TestCase):
    def test_持分会社は会社(self):
        self.assertTrue(issubclass(持分会社, 会社))

    def test_株式会社は会社(self):
        self.assertTrue(issubclass(株式会社, 会社))

    def test_合名会社は持分会社(self):
        self.assertTrue(issubclass(合名会社, 持分会社))

    def test_合名会社は無限責任社員のみで構成される(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertIn(会社.社員[0], [社員])

        with self.assertRaises(Exception) as cm:
            合名会社([有限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '無限責任社員のみ')

    def test_合名会社は所有と経営が一致している(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertEqual(str(会社), '所有と経営が一致')

    def test_合名会社は法人格を持つ(self):
        社員 = 無限責任社員(直接責任())
        会社 = 合名会社([社員])
        self.assertTrue(会社.法人格)

    def test_合資会社は持分会社(self):
        self.assertTrue(issubclass(合資会社, 持分会社))

    def test_合資会社は有限責任社員と無限責任社員で構成される(self):
        社員1 = 有限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合資会社([社員1, 社員2])
        self.assertIn(会社.社員[0], [社員1])
        self.assertIn(会社.社員[1], [社員2])

        with self.assertRaises(Exception) as cm:
            合資会社([有限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '無限責任社員が必要')

        with self.assertRaises(Exception) as cm:
            合資会社([無限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員が必要')

    def test_合資会社は所有と経営が一致している(self):
        社員1 = 有限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合資会社([社員1, 社員2])
        self.assertEqual(str(会社), '所有と経営が一致')

    def test_合資会社は法人格を持つ(self):
        社員1 = 有限責任社員(直接責任())
        社員2 = 無限責任社員(直接責任())
        会社 = 合資会社([社員1, 社員2])
        self.assertTrue(会社.法人格)

    def test_合同会社は持分会社(self):
        self.assertTrue(issubclass(合同会社, 持分会社))

    def test_合同会社は有限責任社員のみで構成される(self):
        社員 = 有限責任社員(間接責任())
        会社 = 合同会社([社員])
        self.assertIn(会社.社員[0], [社員])

        with self.assertRaises(Exception) as cm:
            合同会社([無限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

    def test_合同会社は所有と経営が一致している(self):
        社員 = 有限責任社員(間接責任)
        会社 = 合同会社([社員])
        self.assertEqual(str(会社), '所有と経営が一致')

    def test_合同会社は法人格を持つ(self):
        社員 = 有限責任社員(間接責任)
        会社 = 合同会社([社員])
        self.assertTrue(会社.法人格)

    def test_株式会社は物的会社(self):
        self.assertTrue(issubclass(株式会社, 物的会社))

    def test_株式会社は有限責任社員のみで構成される(self):
        社員 = 有限責任社員(間接責任())
        会社 = 株式会社([社員])
        self.assertIn(会社.社員[0], [社員])

        with self.assertRaises(Exception) as cm:
            株式会社([無限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

    def test_株式会社は所有と経営が分離(self):
        会社 = 株式会社([有限責任社員(間接責任())])
        self.assertEqual(str(会社), '所有と経営が分離')

    def test_特例有限会社は株式会社(self):
        self.assertTrue(issubclass(特例有限会社, 株式会社))

    def test_H18有限責任会社廃止(self):
        with self.assertRaises(Exception) as cm:
            特例有限会社([有限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], 'H18有限会社法廃止')

    def test_有限責任事業組合は持分会社(self):
        self.assertTrue(issubclass(有限責任事業組合, 持分会社))

    def test_有限責任事業組合は所有と経営が一致している(self):
        会社 = 有限責任事業組合([有限責任社員(間接責任), 有限責任社員(間接責任)])
        self.assertEqual(str(会社), '所有と経営が一致')

    def test_有限責任事業組合は有限責任社員2名以上で構成される(self):
        社員1 = 有限責任社員(間接責任())
        社員2 = 有限責任社員(間接責任())
        会社 = 有限責任事業組合([社員1, 社員2])
        self.assertEqual(len(会社.社員), 2)

        with self.assertRaises(Exception) as cm:
            有限責任事業組合([有限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], '構成員2名以上')

        with self.assertRaises(Exception) as cm:
            有限責任事業組合([有限責任社員(間接責任()), 無限責任社員(直接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

        with self.assertRaises(Exception) as cm:
            有限責任事業組合([有限責任社員(間接責任()), 無限責任社員(間接責任())])
        self.assertEqual(cm.exception.args[0], '有限責任社員のみ')

    def test_有限責任事業組合は法人格を持たない(self):
        会社 = 有限責任事業組合([有限責任社員(間接責任), 有限責任社員(間接責任)])
        self.assertFalse(会社.法人格)


class 社員テスト(unittest.TestCase):
    def test_無限責任社員(self):
        self.assertTrue(issubclass(無限責任社員, 社員))

    def test_直接無限責任社員(self):
        社員 = 無限責任社員(直接責任())
        self.assertEqual(type(社員.責任), 直接責任)

    def test_間接無限責任社員(self):
        社員 = 無限責任社員(間接責任())
        self.assertEqual(type(社員.責任), 間接責任)

    def test_有限責任社員(self):
        self.assertTrue(issubclass(有限責任社員, 社員))

    def test_直接有限責任社員(self):
        社員 = 有限責任社員(直接責任())
        self.assertEqual(type(社員.責任), 直接責任)

    def test_間接有限責任社員(self):
        社員 = 有限責任社員(間接責任())
        self.assertEqual(type(社員.責任), 間接責任)


if __name__ == '__main__':
    unittest.main()
