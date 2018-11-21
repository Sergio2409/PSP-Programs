# -*- coding: utf-8 -*-
import math
from linear_regresion_params import LinearRegresionParams
from compute_simpson_rule import ComputeSimpsonRule
from find_t_distribution import FindTDistribution
from listaSE import ListaSE

class Calculate(object):

    def __init__(self, _listx, _listy, E):
        self._listx = _listx
        self._listy = _listy
        self.E = E
        self.lin_regresion = LinearRegresionParams(_listx, _listy)
        self.n = self.lin_regresion.n


    def compute_correlation_significance(self):
        self.r = self.lin_regresion.correlation_r
        t = (abs(self.r)*math.sqrt(self.n-2))/ math.sqrt(1-(self.r**2))
        dof = self.n - 2
        _list = ListaSE()
        _list.add([t, dof])
        self.comp_sim_rule = ComputeSimpsonRule(_list.get(0))
        p = self.comp_sim_rule.compute_integral_value(t, dof, 70)
        self.significance = 1 - (2 * p)

    def compute_std_dev(self):
        self.beta1 = self.lin_regresion.beta1
        self.beta0 = self.lin_regresion.beta0
        self.P = self.lin_regresion.improved_prediction

        _std_dev = 0
        for i in range(self.n):
            xi = self._listx.get(i).value
            yi = self._listy.get(i).value
            _std_dev += (yi - self.beta0 - self.beta1 * xi)**2
        _std_dev *= (self.n-2)**-1
        return _std_dev**0.5


    def compute_70_percent(self):
        std_dev = self.compute_std_dev()
        _list = ListaSE()
        _list.add([0.35, self.n - 2])
        self.t_finder = FindTDistribution(_list.get(0))
        t = self.t_finder.find_specific_t()
        xavg = self.lin_regresion.average(self._listx)
        _sum = 0
        for node in self._listx:
            _sum += (node.value - xavg)**2
        numerator = round((self.E - xavg)**2, 2)
        expre = numerator / _sum
        expre += 1 + (self.n**-1)
        return t * std_dev * math.sqrt(expre)

    def compute_UPI_70(self):
        return self.P + self.compute_70_percent()

    def compute_LPI_70(self):
        return self.P - self.compute_70_percent()

    def all_values(self):
        self.compute_correlation_significance()
        self.compute_std_dev()
        return [
            self.r,
            self.r**2,
            self.significance,
            self.beta0,
            self.beta1,
            self.P,
            self.compute_70_percent(),
            self.compute_UPI_70(),
            self.compute_LPI_70()
        ]
