# -*- coding: utf-8 -*-

import unittest
from application import Application


class TestRelativeSizeChanges(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test1(self):
        self.assertEqual(round(self.app.test1.expected[0], 2),
                         round(self.app.test1._VS, 2))
        self.assertEqual(round(self.app.test1.expected[1], 2),
                         round(self.app.test1._S, 2))
        self.assertEqual(round(self.app.test1.expected[2], 2),
                         round(self.app.test1._M, 2))
        self.assertEqual(round(self.app.test1.expected[3], 2),
                         round(self.app.test1._L, 2))
        self.assertEqual(round(self.app.test1.expected[4], 2),
                         round(self.app.test1._VL, 2))

    def test2(self):
        self.assertEqual(round(self.app.test2.expected[0], 2),
                         round(self.app.test2._VS, 2))
        self.assertEqual(round(self.app.test2.expected[1], 2),
                         round(self.app.test2._S, 2))
        self.assertEqual(round(self.app.test2.expected[2], 2),
                         round(self.app.test2._M, 2))        
        self.assertEqual(round(self.app.test2.expected[3], 3),
                         round(self.app.test2._L, 3))
        self.assertEqual(round(self.app.test2.expected[4], 2),
                         round(self.app.test2._VL, 2))
    

    #  EndClassDefinition


if __name__ == '__main__':
    unittest.main()
