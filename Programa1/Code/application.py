from reader import Reader
from compute_statistics import ComputeStatiscs
from listaSE import ListaSE
from texttable import Texttable


class Application(object):

    def __init__(self):
        self.reader = Reader()
        statiscs = ComputeStatiscs()

        self.lista1 = ListaSE()
        self.lista2 = ListaSE()
        self.set_lista1()
        self.set_lista2()

        self.mean1 = statiscs.compute_mean(self.lista1)
        self.std_dev1 = statiscs.compute_std_dev(self.lista1)
        self.mean2 = statiscs.compute_mean(self.lista2)
        self.std_dev2 = statiscs.compute_std_dev(self.lista2)

    def set_lista1(self):
        lista = self.reader.read_from_file('lista1')
        for el in lista:
            self.lista1.add(el)

    def set_lista2(self):
        lista = self.reader.read_from_file('lista2')
        for el in lista:
            self.lista2.add(el)

    def print_columns(self):
        '''Print a table with the header and rows passed.

        '''
        # Imprimir las dos columnas
        header = [
            ['Columna1', 'Columna2'],
            ['Estimated Proxy Size', 'Development Hours']
        ]
        rows = []
        for pos in range(self.lista1.size):
            rows.append([self.lista1.get(pos), self.lista2.get(pos)])

        table = Texttable()
        table.set_cols_align(["l", "r"])
        table.set_cols_valign(["t", "m"])
        table.add_rows(header + rows)
        print(table.draw() + "\n")

    def print_table(self):
        '''Print a table with the header and rows passed.

        '''
        # Imprimir los resultados de media y desviacion estandar
        header = [
            ['Test', 'Actual Value', 'Actual Value'],
            ['', 'Mean', 'Std. Dev']
        ]
        rows = [
            ['Column1', self.mean1, self.std_dev1],
            ['Column2', self.mean2, self.std_dev2]
        ]

        table = Texttable()
        table.set_cols_align(["c", "c", "c"])
        table.set_cols_valign(["t", "m", "b"])
        table.add_rows(header + rows)
        print(table.draw() + "\n")


if __name__ == "__main__":
    app = Application()
    app.print_columns()
    app.print_table()
