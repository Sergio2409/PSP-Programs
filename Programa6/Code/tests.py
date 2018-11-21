# -*- coding: utf-8 -*-

import unittest
from application import Application


class TestRelativeSizeChanges(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test1(self):
        self.assertEqual(self.app.test1.expected,
                         round(self.app.results[0].find_specific_t(), 5))

    def test2(self):
        self.assertEqual(self.app.test2.expected,
                         round(self.app.results[1].find_specific_t(), 5))

    def test3(self):
        self.assertEqual(round(self.app.test3.expected, 3),
                         round(self.app.results[2].find_specific_t(), 3))


    #  EndClassDefinition


if __name__ == '__main__':
    unittest.main()
