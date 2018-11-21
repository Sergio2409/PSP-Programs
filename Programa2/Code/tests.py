# -*- coding: utf-8 -*-

import unittest
from counter_loc import CounterLOC


class TestCounterLOC(unittest.TestCase):

    def test_size_program1(self):
        path = '/home/sergio/work/maestria-2018/IngenieriaSW/Programas PSP/Programa1/Code'
        loc_counter1 = CounterLOC(path)
        self.assertEqual(loc_counter1.classes[0].total_lines_of_codes, 12)
        self.assertEqual(loc_counter1.classes[1].total_lines_of_codes, 59)
        self.assertEqual(loc_counter1.classes[2].total_lines_of_codes, 61)
        self.assertEqual(loc_counter1.classes[3].total_lines_of_codes, 15)
        self.assertEqual(loc_counter1.classes[4].total_lines_of_codes, 17)
        self.assertEqual(loc_counter1.classes[5].total_lines_of_codes, 11)
        self.assertEqual(loc_counter1.total_lines_of_codes, 175)

    def test_size_program2(self):
        path = '/home/sergio/work/maestria-2018/IngenieriaSW/Programas PSP/Programa2/Code'
        loc_counter2 = CounterLOC(path)
        self.assertEqual(loc_counter2.classes[0].total_lines_of_codes, 10)
        self.assertEqual(loc_counter2.classes[1].total_lines_of_codes, 35)
        self.assertEqual(loc_counter2.classes[2].total_lines_of_codes, 23)
        self.assertEqual(loc_counter2.classes[3].total_lines_of_codes, 56)
        self.assertEqual(loc_counter2.total_lines_of_codes, 124)

    #  EndClassDefinition


if __name__ == '__main__':
    unittest.main()
