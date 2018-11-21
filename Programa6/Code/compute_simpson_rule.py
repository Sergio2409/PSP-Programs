# -*- coding: utf-8 -*-
import math
from math import log, sqrt, e

class ComputeSimpsonRule(object):

    def __init__(self, _list):
        self.t = _list.value[0]
        self.dof = _list.value[1]
        self.p = 0


    def compute_factorial(self, val):
        ''' Calcula el factorial del número pasado (val – 1).

        '''
        for el in range(2, val):
            val *= el
        return val

    def compute_gamma(self, val):
        '''Calcula el valor gamma, si el valor es ´int´: se calcula de la
        siguiente forma:
        gamma = (val – 1)!
        Si el valor es el valor es ´float´ entonces se calcula:
        gamma = (val-1) gamma (x-1) teniendo en cuenta que:
        gamma (1) = 1
        gamma (1/2) = sqrt (Pi)'

        '''
        res = 0
        val -= 1
        if not isinstance(val, int) :
            res = val
            new_val = 0
            while val > 0:
                new_val = val - 1
                if new_val > 0:
                    res *= new_val
                val -= 1
        else:
            return self.compute_factorial(val)
        return res * math.sqrt(math.pi)

    def not_pair(self, val):
        '''Esta función recive un valor numérico en caso de que ese valor no
        sea divisible  por 2, devuelve ese valor convertido a ´ float´ sino
        devuelve el mismo número.

        '''
        return float(val) if val%2 != 0 else val

    def compute_function_Xi(self, Xi, dof, _gmma_num, _gmma_denom):
        '''Calcular el valor de la función con la regla de Simpson para
        integrar la densidad de probabilidad usando la siguiente ecuación.

        '''
        F_0 = 0
        Pi = math.pi
        _b_F0 = 1 + (math.pow(Xi, 2)/dof)
        exp_more = float(dof+1)
        exp = -(exp_more / 2)
        F_0 = math.pow(_b_F0, exp)
        F = _gmma_num / (math.pow(dof*Pi, 0.5) * _gmma_denom) * F_0
        return F

    def compute_integral_value(self, val, dof, num_seg):
        ini_val, sum_by_2, sum_by_4, end_val = 0, 0, 0, 0
        Xi, sum_terms, p = 0, 0, 0

        W = val/num_seg
        dof_pls_one = self.not_pair(dof+1)
        dof = self.not_pair(dof)
        _gmma_num = self.compute_gamma(dof_pls_one/2)
        _gmma_denom = self.compute_gamma(dof/2)

        pos = 0
        while pos < num_seg:
            sum_2, sum4 = 0, 0
            Xi = pos * W
            if pos == 0:
                ini_val = self.compute_function_Xi(Xi, dof, _gmma_num,
                                                   _gmma_denom)
            elif pos%2 == 0 and pos != 0:
                sum_2 = self.compute_function_Xi(Xi, dof, _gmma_num, _gmma_denom)
                sum_by_2 += 2 * sum_2
            else:
                sum_4 = self.compute_function_Xi(Xi, dof, _gmma_num, _gmma_denom)
                sum_by_4 += 4 * sum_4
            pos += 1
        end_val = self.compute_function_Xi(val, dof, _gmma_num, _gmma_denom)
        terms_sums = ini_val + sum_by_2 + sum_by_4 + end_val
        p = terms_sums * (W/3)
        return p

    def compute_total_probability(self):
        self.p, p_0, p_1 = 0, 0, 0
        E = 0.0000001
        res = []
        p_0 = round(self.compute_integral_value(self.t, self.dof, 10), 5)
        p_1 = round(self.compute_integral_value(self.t, self.dof, 20), 5)
        _abs = abs(p_0 - p_1)
        if _abs >= E:
            print('Error: The absolute value |%f-%f| > %f' % (p_0,p_1,E))
        else:
            self.p = p_1
        return self.p
