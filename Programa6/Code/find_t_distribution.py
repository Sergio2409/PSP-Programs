#!/usr/bin/env python
from compute_simpson_rule import ComputeSimpsonRule
from listaSE import ListaSE


class FindTDistribution(object):

    def __init__(self, _list):
        self.t = 0
        self.dof = _list.value[1]
        self.p = _list.value[0]

        self.comp_sim_rule = ComputeSimpsonRule(_list)

    def find_specific_t(self):
        '''Find the `t` distribution which is used to obtain a value of _p
        that the rest of `self.p` - `_p` it's lest than an E = 0.0000001.

        '''
        E = 0.0000001
        ten_sec = 10
        thirt_sec = 30
        t_found = False
        ini_t = 1.0
        d = 0.5
        prev_error = None
        while not t_found:
            _p = self.comp_sim_rule.compute_integral_value(ini_t,
                                                           self.dof,
                                                           thirt_sec)
            _error = _p - self.p
            if _error == 0 or abs(_error) < E:
                t_found = True
            else:
                if prev_error:
                    sign_changed = (prev_error < 0 and _error > 0) or (prev_error > 0 and _error < 0)
                    if sign_changed:
                        d = d/2
                if _p < self.p:
                    ini_t += d
                else:
                    ini_t -= d
            prev_error = _error
        self.t = ini_t
        return ini_t
