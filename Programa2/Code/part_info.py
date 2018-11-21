# -*- coding: utf-8 -*-


class PartInfo(object):

    def __init__(self, name):
        self.name = name
        self.methods_count = 0
        self.class_lines = 0
        self.import_lines = 0
        self.external_lines = 0

    @property
    def total_lines_of_codes(self):
        return self.import_lines + self.class_lines + self.external_lines
