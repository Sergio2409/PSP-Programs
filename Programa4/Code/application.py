# -*- coding: utf-8 -*-

from texttable import Texttable
from reader import Reader
from listaSE import ListaSE
from relative_size_changes import RelativeSizeChanges


class Application(object):

    def __init__(self):
        self.reader = Reader()
        self.load_data()

        self._list1 = self.get_list_from_data(self.data1)
        self.test1 = RelativeSizeChanges(self._list1)
        self._list2 = self.get_list_from_data(self.data2)
        self.test2 = RelativeSizeChanges(self._list2)
        self.test1.name = 'LOC/Method'
        self.test2.name = 'Pgs/Chapter'    
        self.test1.expected = [4.3953, 8.5081, 16.4696, 31.8811, 61.7137]
        self.test2.expected = [6.3375, 8.4393, 11.2381, 14.9650, 19.9280]     
        
        self.results = [self.test1, self.test2]

    def load_data(self):
        '''Load the data needed to test the application

        Loads the four test data to be used for compute linear regression
        params.

        '''
        self.data1 = self.reader.read_from_file('test_data1.txt')
        self.data2 = self.reader.read_from_file('test_data2.txt')        

    def get_list_from_data(self, data):
        '''Return the corresponding listX and listY from the passed data.

        '''
        _list = ListaSE()        
        for line in data:
            x, y = line.split()
            if y == '0':
                raise ZeroDivisionError('The second value must not be zero!')
            _list.add(float(x)/float(y))            
        return _list

    def draw_table_result(self):
        '''Print a table with the header and rows passed.

        '''
        # Imprimir las dos columnas
        header = [['' , 'VS', 'S', 'M', 'L', 'VL']]
        total = 0
        for test in self.results:
            header.append([test.name, test._VS, test._S, test._M, test._L, test._VL])        
        table = Texttable()
        table.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.HLINES | Texttable.BORDER)
        table.set_cols_align(["c", "c", "c", "c", "c", "c"])
        table.set_cols_valign(["m", "m", "m", "m", "m", "m"])
        table.add_rows(header)
        print(table.draw() + "\n")

    #  EndClassDefinition


if __name__ == "__main__":
    print('Welcome to PSP Program4!')
    app = Application()
    app.draw_table_result()
