# -*- coding: utf-8 -*-

import unittest
from application import Application


class TestRelativeSizeChanges(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test1(self):
        self.assertEqual(self.app.test1.expected,
                         self.app.results[0].compute_total_probability())

    def test2(self):
        self.assertEqual(self.app.test2.expected,
                         self.app.results[1].compute_total_probability())

    def test3(self):
        self.assertEqual(self.app.test3.expected,
                         self.app.results[2].compute_total_probability())


    #  EndClassDefinition


if __name__ == '__main__':
    unittest.main()
