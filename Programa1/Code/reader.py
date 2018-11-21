# -*- coding: utf-8 -*-
import os


class Reader(object):

    def read_from_file(self, filename):
        '''Return a list with each line of the file path passed.

        '''
        if os.path.exists(filename):
            file = open(filename, 'r')
            lines = file.readlines()
            file.close()
            return [float(num) for num in lines]
        else:
            raise ValueError('The file passed does not exists!')
