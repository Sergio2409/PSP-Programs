# -*- coding: utf-8 -*-

import unittest
from application import Application


class TestRelativeSizeChanges(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test1(self):
        test = self.app.test1
        for pos in range(len(self.app.paramters)):
            current_values = test.all_values()
            self.assertEqual(round(test.expected[pos], 3),
                             round(current_values[pos], 3))

    def test2(self):
        test = self.app.test2
        for pos in range(len(self.app.paramters)):
            current_values = test.all_values()
            self.assertEqual(round(test.expected[pos], 3),
                             round(current_values[pos], 3))


    #  EndClassDefinition


if __name__ == '__main__':
    unittest.main()
