# -*- coding: utf-8 -*-

import unittest
from application import Application


class TestLinearRegresionParams(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test1(self):
        self.assertEqual(round(self.app.test1.expected[0], 2),
                         round(self.app.test1.beta0, 2))
        self.assertEqual(round(self.app.test1.expected[1], 2),
                         round(self.app.test1.beta1, 2))
        self.assertEqual(round(self.app.test1.expected[2], 2),
                         round(self.app.test1.correlation_r, 2))
        self.assertEqual(round(self.app.test1.expected[3], 2),
                         round(self.app.test1.correlation_r**2, 2))
        self.assertEqual(round(self.app.test1.expected[4], 2),
                         round(self.app.test1.improved_prediction, 2))

    def test2(self):
        self.assertEqual(round(self.app.test2.expected[0], 2),
                         round(self.app.test2.beta0, 2))
        self.assertEqual(round(self.app.test2.expected[1], 2),
                         round(self.app.test2.beta1, 2))
        self.assertEqual(round(self.app.test2.expected[2], 2),
                         round(self.app.test2.correlation_r, 2))
        self.assertEqual(round(self.app.test2.expected[3], 2),
                         round(self.app.test2.correlation_r**2, 2))
        self.assertEqual(round(self.app.test2.expected[4], 2),
                         round(self.app.test2.improved_prediction, 2))

    def test3(self):
        self.assertEqual(round(self.app.test3.expected[0], 2),
                         round(self.app.test3.beta0, 2))
        self.assertEqual(round(self.app.test3.expected[1], 2),
                         round(self.app.test3.beta1, 2))
        self.assertEqual(round(self.app.test3.expected[2], 2),
                         round(self.app.test3.correlation_r, 2))
        self.assertEqual(round(self.app.test3.expected[3], 2),
                         round(self.app.test3.correlation_r**2, 2))
        self.assertEqual(round(self.app.test3.expected[4], 2),
                         round(self.app.test3.improved_prediction, 2))

    def test4(self):
        self.assertEqual(round(self.app.test4.expected[0], 2),
                         round(self.app.test4.beta0, 2))
        self.assertEqual(round(self.app.test4.expected[1], 2),
                         round(self.app.test4.beta1, 2))
        self.assertEqual(round(self.app.test4.expected[2], 2),
                         round(self.app.test4.correlation_r, 2))
        self.assertEqual(round(self.app.test4.expected[3], 2),
                         round(self.app.test4.correlation_r**2, 2))
        self.assertEqual(round(self.app.test4.expected[4], 2),
                         round(self.app.test4.improved_prediction, 2))

    #  EndClassDefinition


if __name__ == '__main__':
    unittest.main()
