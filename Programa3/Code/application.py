# -*- coding: utf-8 -*-

from texttable import Texttable
from reader import Reader
from listaSE import ListaSE
from linear_regresion_params import LinearRegresionParams


class Application(object):

    def __init__(self):
        self.reader = Reader()
        self.load_data()

        x, y = self.get_list_from_data(self.data1)
        self.test1 = LinearRegresionParams(x, y)
        x, y = self.get_list_from_data(self.data2)
        self.test2 = LinearRegresionParams(x, y)
        x, y = self.get_list_from_data(self.data3)
        self.test3 = LinearRegresionParams(x, y)
        x, y = self.get_list_from_data(self.data4)
        self.test4 = LinearRegresionParams(x, y)

        self.test1.expected = [-22.55, 1.7279, 0.9545, 0.9111, 644.429]
        self.test2.expected = [-4.039, 0.1681, 0.9333, 0.8711, 60.858]
        self.test3.expected = [-23.92, 1.43097, 0.9631, 0.9276, 528.4294]
        self.test4.expected = [-4.604, 0.140164, 0.9480, 0.8988, 49.4994]

        self.results = [self.test1, self.test2, self.test3, self.test4]

    def load_data(self):
        '''Load the data needed to test the application

        Loads the four test data to be used for compute linear regression
        params.

        '''
        self.data1 = self.reader.read_from_file('test_data1.txt')
        self.data2 = self.reader.read_from_file('test_data2.txt')
        self.data3 = self.reader.read_from_file('test_data3.txt')
        self.data4 = self.reader.read_from_file('test_data4.txt')

    def get_list_from_data(self, data):
        '''Return the corresponding listX and listY from the passed data.

        '''
        _list_x = ListaSE()
        _list_y = ListaSE()
        for line in data:
            x, y = line.split()
            _list_x.add(float(x))
            _list_y.add(float(y))
        return _list_x, _list_y

    def draw_table_result(self):
        '''Print a table with the header and rows passed.

        '''
        # Imprimir las dos columnas
        header = [['Test', 'Expeceted Values\nBeta0 | Beta1 | r | r*r | P',
                   'Actual Values\nBeta0 | Beta1 | r | r*r | P']]
        rows = []

        total = 0
        for num, test in enumerate(self.results):
            header.append(
                ['Test {0}'.format(str(num+1)),
                 '{0} | {1} | {2} | {3} | {4}'.format(
                     test.expected[0], test.expected[1],
                     test.expected[2], test.expected[3],
                     test.expected[4]),
                 '{0} | {1} | {2} | {3} | {4}'.format(
                     test.beta0, test.beta1,
                     test.correlation_r, test.correlation_r**2,
                     test.improved_prediction)])
        rows.append(['', '', '', '', '', total])
        table = Texttable()
        table.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.HLINES | Texttable.BORDER)
        table.set_cols_align(["c", "c", "c"])
        table.set_cols_valign(["m", "m", "m"])
        table.add_rows(header)
        print(table.draw() + "\n")

    #  EndClassDefinition


if __name__ == "__main__":
    print('Welcome to PSP Program3!')
    app = Application()
    app.draw_table_result()
