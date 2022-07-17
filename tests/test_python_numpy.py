import unittest

from python_numpy.net import Net


class MainTestCase(unittest.TestCase):
    def setUp(self):
        weigths1 = [
            [0.3, 0.3, 0],
            [0.4, -0.5, 1],
        ]
        weights2 = [
            [-1, 1],
        ]
        neurons1 = [Net.perceptron, Net.perceptron]
        neurons2 = [Net.perceptron]
        self.net = Net([weigths1, weights2], [neurons1, neurons2], use_bias=False)

    def test000(self):
        res = self.net.go([0, 0, 0])
        self.assertEqual(res, 0)

    def test001(self):
        res = self.net.go([0, 0, 1])
        self.assertEqual(res, 1)

    def test010(self):
        res = self.net.go([0, 1, 0])
        self.assertEqual(res, 0)

    def test011(self):
        res = self.net.go([0, 1, 1])
        self.assertEqual(res, 1)

    def test100(self):
        res = self.net.go([1, 0, 0])
        self.assertEqual(res, 0)

    def test101(self):
        res = self.net.go([1, 0, 1])
        self.assertEqual(res, 1)

    def test110(self):
        res = self.net.go([1, 1, 0])
        self.assertEqual(res, 0)

    def test111(self):
        res = self.net.go([1, 1, 1])
        self.assertEqual(res, 0)


"""class AndTestCase(unittest.TestCase):
    def setUp(self):
        weigths1 = [
            [0.3, 1],
        ]
        self.net = Net([weigths1])

    def test00(self):
        res = self.net.go([0, 0])
        self.assertEqual(res, 0)

    def test01(self):
        res = self.net.go([0, 1])
        self.assertEqual(res, 0)

    def test10(self):
        res = self.net.go([1, 0])
        self.assertEqual(res, 0)

    def test11(self):
        res = self.net.go([1, 1])
        self.assertEqual(res, 1)"""


class OrTestCase(unittest.TestCase):
    def setUp(self):
        weigths1 = [
            [2.5, 5.5, -0.5],
        ]
        neurons1 = [Net.perceptron]
        self.net = Net([weigths1], [neurons1])

    def test00(self):
        res = self.net.go([0, 0])
        self.assertEqual(res, 0)

    def test01(self):
        res = self.net.go([0, 1])
        self.assertEqual(res, 1)

    def test10(self):
        res = self.net.go([1, 0])
        self.assertEqual(res, 1)

    def test11(self):
        res = self.net.go([1, 1])
        self.assertEqual(res, 1)


class XorTestCase(unittest.TestCase):
    def setUp(self):
        weigths1 = [
            [-9.5, 5.5, 4.5, ],
            [-8.5, 4.5, -0.5],
        ]
        weights2 = [
            [-3.5, 0.5, 3.5],
        ]
        neurons1 = [Net.perceptron, Net.perceptron]
        neurons2 = [Net.perceptron]
        self.net = Net([weigths1, weights2], [neurons1, neurons2])

    def test00(self):
        res = self.net.go([0, 0])
        self.assertEqual(res, 0)

    def test01(self):
        res = self.net.go([0, 1])
        self.assertEqual(res, 1)

    def test10(self):
        res = self.net.go([1, 0])
        self.assertEqual(res, 1)

    def test11(self):
        res = self.net.go([1, 1])
        self.assertEqual(res, 0)
