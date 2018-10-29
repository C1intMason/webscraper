import xlsxwriter



book = xlsxwriter.Workbook("test.xlsx")
sheet = book.add_worksheet()
sheet.set_column(1, 1, 30)

bold = book.add_format({'bold': True})

sheet.write('A1', 'Title', bold)
sheet.write('A2', 'content')
sheet.write(3, 0, 123.456)


