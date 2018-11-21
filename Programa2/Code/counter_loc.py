# -*- coding: utf-8 -*-

import glob
from part_info import PartInfo


class CounterLOC(object):

    def __init__(self, path_folder):
        self.path_folder = path_folder
        self.classes = []
        self.all_files = self.get_all_files()
        for file in self.all_files:
            self.process_file(file)

    @property
    def total_lines_of_codes(self):
        return sum([_class.total_lines_of_codes for _class in self.classes])

    def get_all_files(self):
        '''Return all files inside the path folder.

        '''
        return glob.glob(self.path_folder + "/*.py")

    def is_valid_line(self, line):
        '''Returns True if the line must be count otherwise returns False.'''
        return not (line.startswith('#') or line.isspace() or line is '')

    def process_file(self, file_path):
        '''Process the passed file detecting class definition, number of
        methods for the class, total lines of codes for the class and lines
        count for imports

        '''
        with open(file_path, 'r') as f:
            all_lines = f.readlines()
        f.closed

        _class_lines_count = 0
        import_lines_count = 0
        methods_count = 0
        part_info = None
        external_class_lines = 0
        end_class_definition_found = False

        for line in all_lines:
            line = line.strip()
            if self.is_valid_line(line):
                if line.startswith('class'):
                    name = line.split()[1].split('(')[0]
                    part_info = PartInfo(name)
                elif line.startswith('def'):
                    methods_count += 1

                if end_class_definition_found:
                    external_class_lines += 1
                else:
                    if line.startswith('import') or line.startswith('from'):
                        import_lines_count += 1
                    else:
                        _class_lines_count += 1
            else:
                if line.find('EndClassDefinition') > 0:
                    end_class_definition_found = True

        part_info.methods_count = methods_count
        part_info.import_lines = import_lines_count
        part_info.class_lines = _class_lines_count
        part_info.external_lines = external_class_lines
        self.classes.append(part_info)
