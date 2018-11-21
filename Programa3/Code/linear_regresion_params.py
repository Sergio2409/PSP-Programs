# -*- coding: utf-8 -*-


class LinearRegresionParams(object):

    def __init__(self, _list_x, _list_y):
        self._list_x = _list_x
        self._list_y = _list_y

        self.x_avg = self.average(self._list_x)
        self.y_avg = self.average(self._list_y)

        self.mult_summ = self.multiplication_lists_summation(self._list_x,
                                                             self._list_y)
        self.x_squaring_sum = self.squaring_summation(self._list_x)

    @property
    def n(self):
        if self._list_x.size == self._list_y.size:
            return self._list_x.size
        else:
            raise ValueError('The lists must have the same size!')

    def average(self, _list):
        '''Returns the average for list passed

        '''
        average = 0
        for node in _list:
            average += node.value
        return average/_list.size

    def list_summation(self, _list):
        '''Returns the summation of all elements from the passed list

        '''
        _sum = 0
        for node in _list:
            _sum += node.value
        return _sum

    def multiplication_lists_summation(self, _list1, _list2):
        '''Returns the summation of multiplication for each 'i'-elements from
        the passed lists

        '''
        _sum = 0
        for pos in range(_list1.size):
            _sum += _list1.get(pos).value * _list2.get(pos).value
        return _sum

    def squaring_summation(self, _list):
        '''Returns the summation of each element squared from the passed list.

        '''
        _sum = 0
        for node in _list:
            _sum += self.squaring(node.value)
        return _sum

    @property
    def beta1(self):
        '''Compute the linear regression param Beta1

        '''
        numerator = self.mult_summ - (self.n * self.x_avg * self.y_avg)
        denominator = self.x_squaring_sum - self.n * self.squaring(self.x_avg)
        if denominator == 0:
            raise ValueError('Denominator must not be 0!')
        return numerator / denominator

    @property
    def beta0(self):
        '''Compute the linear regression param Beta0

        '''
        return self.y_avg - (self.beta1 * self.x_avg)

    @property
    def correlation_r(self):
        '''Compute the linear regression param Beta1

        '''
        sum_x = self.list_summation(self._list_x)
        sum_y = self.list_summation(self._list_y)
        numerator = self.n * self.mult_summ - (sum_x * sum_y)
        y_squaring_sum = self.squaring_summation(self._list_y)
        denom_left = self.n * self.x_squaring_sum - self.squaring(sum_x)
        denom_rigth = self.n * y_squaring_sum - self.squaring(sum_y)
        return numerator / ((denom_left * denom_rigth)**0.5)

    @property
    def improved_prediction(self):
        '''Compute linear regression param P

        '''
        E = 386
        return self.beta0 + self.beta1 * E

    def squaring(self, number):
        '''Return the number passed squared.

        '''
        return number**2
