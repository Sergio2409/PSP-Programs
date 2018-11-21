# -*- coding: utf-8 -*-

import unittest
from application import Application


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_mean1(self):
        self.assertEqual(self.app.mean1, 550.6)

    def test_mean2(self):
        self.assertEqual(self.app.mean2, 60.32)

    def test_std_dev1(self):
        self.assertEqual(self.app.std_dev1, 572.03)

    def test_std_dev2(self):
        self.assertEqual(self.app.std_dev2, 62.26)

    #  EndClassDefinition


if __name__ == '__main__':
    unittest.main()
