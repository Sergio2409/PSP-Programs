# -*- coding: utf-8 -*-
from math import log, sqrt, e

class RelativeSizeChanges(object):

    def __init__(self, _list):
        self._list = _list 

    @property
    def n(self):
        return self._list.size

    @property
    def ln_xi(self):    
        return [log(el.value) for el in self._list]

    @property
    def average(self):
        '''Returns the average for list passed

        '''
        average = 0
        for node in self.ln_xi:
            average += node        
        return average/self.n

    def list_summation(self, _list):
        '''Returns the summation of all elements from the passed list

        '''
        _sum = 0
        for node in _list:
            _sum += node
        return _sum

    @property
    def variance(self):
        '''Compute the variance of the list values

        '''        
        num = [(el - self.average)**2 for el in self.ln_xi]
        return self.list_summation(num)/(self.n - 1)

    @property
    def compute_st_deviation(self):
        '''Compute the standart deviation of the list.

        '''        
        return sqrt(self.variance)

    @property
    def _VS(self):
        '''Compute very small ranges

        '''        
        return e**(self.average - 2 * self.compute_st_deviation)

    @property
    def _S(self):
        '''Compute small ranges

        '''        
        return e**(self.average - self.compute_st_deviation)

    @property
    def _M(self):
        '''Compute large ranges

        '''
        return e**(self.average)

    @property
    def _L(self):
        '''Compute large ranges

        '''
        return e**(self.average + self.compute_st_deviation)

    @property
    def _VL(self):
        '''Compute very large ranges using standard deviation of an assumed
        log-normal distribution of sizes.

        '''
        return e**(self.average + 2 * self.compute_st_deviation)
