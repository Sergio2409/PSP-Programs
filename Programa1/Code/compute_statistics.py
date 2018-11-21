# -*- coding: utf-8 -*-
import math


class ComputeStatiscs(object):

    def compute_mean(self, list_num):
        '''Compute the average of the passed number list.

        '''
        average = 0
        for node in list_num:
            average += node.value
        return round(average/list_num.size, 2)

    def compute_std_dev(self, list_num):
        '''Compute the standard deviation of of the passed number list.

        '''

        media = self.compute_mean(list_num)
        std_dev = 0
        for node in list_num:
            std_dev += (node.value - media)**2
        return round(math.sqrt((std_dev/(list_num.size-1))), 2)
