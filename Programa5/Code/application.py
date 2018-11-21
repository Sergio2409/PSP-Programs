# -*- coding: utf-8 -*-

from texttable import Texttable
from reader import Reader
from listaSE import ListaSE
from find_t_distribution import FindTDistribution


class Application(object):

    def __init__(self):
        self.reader = Reader()
        self.load_data()

        self.data = self.get_list_from_data(self.data1)
        self.test1 = FindTDistribution(self.data.get(0))
        self.test2 = FindTDistribution(self.data.get(1))
        self.test3 = FindTDistribution(self.data.get(2))

        self.test1.expected = 0.55338
        self.test2.expected = 1.75305
        self.test3.expected = 4.60409
        self.results = [self.test1,
                        self.test2,
                        self.test3]

    def load_data(self):
        '''Load the data needed to test the application

        Loads the four test data to be used for compute linear regression
        params.

        '''
        self.data1 = self.reader.read_from_file('test_data1.txt')

    def get_list_from_data(self, data):
        '''Return the corresponding listX and listY from the passed data.

        '''
        _list = ListaSE()
        for line in data:
            x, y = line.split()
            if y == '0':
                raise ZeroDivisionError('The second value must not be zero!')
            _list.add([float(x), int(y)])
        return _list

    def draw_table_result(self):
        '''Print a table with the header and rows passed.

        '''
        # Imprimir las dos columnas
        header = [['p' , 'dof', 't(expected)', 't(actual)']]
        total = 0
        for test in self.results:
            header.append([
                test.p,
                test.dof,
                test.expected,
                test.find_specific_t()])
        table = Texttable()
        table.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.HLINES | Texttable.BORDER)
        table.set_cols_align(["c", "c", "c", "c"])
        table.set_cols_valign(["m", "m", "m", "m"])
        table.add_rows(header)
        print(table.draw() + "\n")

    #  EndClassDefinition


if __name__ == "__main__":
    print('Welcome to PSP Program4!')
    app = Application()
    app.draw_table_result()
