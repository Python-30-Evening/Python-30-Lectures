""" CSV """
# CSV - Comma Separated Values - данные разделенные запятой. Формат файлов табличного вида


import csv

with open('laptops.csv', 'w') as table:
    writer = csv.writer(table)
    writer.writerow(['title', 'price', 'description'])
    writer.writerow(['Samsung', 1234123, 'Cool phone'])
