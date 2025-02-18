# tableformat.py

class FormatError(Exception):
    pass

class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise  NotImplementedError()
    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f"<th>{h}</th>", end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for h in rowdata:
            print(f"<td>{h}</td>", end='')
        print('</tr>')

def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')


def print_table(portfile, columns, formatter):
    formatter.headings(columns)
    # Get row data
    for each_stock in portfile:
        rowdata = [str(getattr(each_stock, colname)) for colname in columns]
        formatter.row(rowdata)
