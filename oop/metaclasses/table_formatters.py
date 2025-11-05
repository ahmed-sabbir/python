import sys
from abc import ABCMeta, abstractmethod

'''
python -i portfolio.py
import table
formatter = table.TextTableFormatter()
table.print_table(portfolio, ['name','shares'], formatter)

class MyFormatter(table_formatters.TableFormatter):
    name='spam'
  
table_formatters._formatters
'''

def print_table(objects, colnames):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''
    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    for object in objects:
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(object, colname))), end=' ')
        print()

def print_table(objects, column_names, formatter):
    '''
    Returns a formatted response (according to the formatter passed) showing attributes from a list of objects
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError('formatter must be a TableFormatter')
     
    formatter.headings(column_names)
    for object in objects:
        rowData = [str(getattr(object, column_name)) for column_name in column_names]
        formatter.row(rowData)

_formatters = {}

class TableMeta(ABCMeta):
    def __init__(cls, clsname, bases, methods):
        super().__init__(clsname, bases, methods)
        if hasattr(cls, 'name'):
            _formatters[cls.name] = cls 

'''
metaclass is used to supervise a collection of classes
'''
class TableFormatter(metaclass=TableMeta):
    '''
    Serves as a design specification for making tables
    '''
    def __init__(self, outfile=None):
        if outfile == None:
            self.outfile = sys.stdout
        self.outfile = outfile

    @abstractmethod
    def headings(self, headers):
        pass
    
    @abstractmethod
    def row(self, rowData):
        pass


class TextTableFormatter(TableFormatter):
    name = 'text'
    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

    def row(self, rowData):
        for row in rowData:
            print('{:>{}s}'.format(row, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

class CSVTableFormatter(TableFormatter):
    name = 'csv'
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowData):
        print(','.join(rowData))

class HTMLTableFormatter(TableFormatter):
    name = 'html'
    def headings(self, headers):
        print('<tr>', end=' ')
        for header in headers:
            print('<th>{}</th>'.format(header),end=' ')
        print('</tr>')

    def row(self, rowData):
        print('<tr>', end=' ')
        for row in rowData:
            print('<td>{}</td>'.format(row), end=' ')
        print('</tr>')

def create_format(name):
    formatter = _formatters.get(name)
    if not formatter:
        raise ValueError('Unknown format {}'.format(name))
    return formatter()