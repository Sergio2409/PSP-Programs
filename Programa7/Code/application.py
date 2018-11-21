# -*- coding: utf-8 -*-

from texttable import Texttable
from reader import Reader
from listaSE import ListaSE
from calculate import Calculate


class Application(object):

    def __init__(self):
        self.reader = Reader()
        self.load_data()

        x, y = self.get_list_from_data(self.data1)
        self.test1 = Calculate(x, y, 386)
        x, y = self.get_list_from_data(self.data2)
        self.test2 = Calculate(x, y, 386)
        x, y = self.get_list_from_data(self.data3)
        self.test3 = Calculate(x, y, 118)
        x, y = self.get_list_from_data(self.data4)
        self.test4 = Calculate(x, y, 118)

        self.paramters = ['r', 'r*r', 'Significance', 'beta0', 'beta1', 'P',
                          'Range', 'UPI (70%)', 'LPI (70%)']

        self.test1.expected = [0.954496574, 0.91106371, 1.77517*10**-5,
                               -22.55253275, 1.727932426, 644.4293838,
                               230.0017197, 874.4311035, 414.427664]
        self.test2.expected = [0.933306898, 0.871061766, 7.98203*10**-5,
                               -4.038881575, 0.16812665, 60.85800528,
                               27.55764748, 88.41565276, 33.3003578]

        self.test3.expected = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.test4.expected = [0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        header = [['Test' , 'Parameter', 't(expected)', 't(actual)']]
        total = 0
        for num, test in enumerate(self.results):
            for pos in range(len(self.paramters)):
                current_values = test.all_values()
                header.append([
                    'Test{0}'.format(str(num + 1)),
                    self.paramters[pos],
                    test.expected[pos],
                    current_values[pos]])
        table = Texttable()
        table.set_precision(6)
        table.set_cols_align(["c", "c", "c", "c"])
        table.set_cols_valign(["m", "m", "m", "m"])
        table.add_rows(header)
        print(table.draw() + "\n")

    #  EndClassDefinition


if __name__ == "__main__":
    print('Welcome to PSP Program6!')
    app = Application()
    app.draw_table_result()
