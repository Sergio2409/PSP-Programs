# -*- coding: utf-8 -*-

import os
from texttable import Texttable
from counter_loc import CounterLOC


class Application(object):

    def __init__(self, path_folder):
        self.loc_counter = CounterLOC(path_folder)

    def draw_table_result(self):
        '''Print a table with the header and rows passed.

        '''
        # Imprimir las dos columnas
        header = [
            ['Part Name', 'Number of Items', 'Import lines', 'Class lines',
             'External lines', 'Total']
        ]
        rows = []

        total = 0
        for part_info in self.loc_counter.classes:
            total += part_info.total_lines_of_codes
            rows.append([part_info.name, part_info.methods_count,
                         part_info.import_lines, part_info.class_lines,
                         part_info.external_lines,
                         part_info.total_lines_of_codes])
        rows.append(['', '', '', '', '', total])
        table = Texttable()
        table.set_cols_align(["c", "c", "c", "c", "c", "c"])
        table.set_cols_valign(["m", "m", "m", "m", "m", "m"])
        table.add_rows(header + rows)
        print(table.draw() + "\n")

    #  EndClassDefinition


if __name__ == "__main__":
    print('Welcome to Lines of Code counter!')
    msg = 'Entre la carpeta donde se encuentran los archivos a contar: \n'
    path = raw_input(msg)
    while not os.path.isdir(path):
        path = raw_input(msg)
    app = Application(path)
    app.draw_table_result()
