import csv
from itertools import groupby

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [row for row in csv_reader if len(row) > 0]
    grouped_data = [list(i) for j, i in groupby(data, lambda a: a[0])]
    for row in grouped_data:
    	print(row[0][0])

# f = open("test.md", "w")
# f.write("Created file")