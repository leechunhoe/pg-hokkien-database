import csv

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [row for row in csv_reader if len(row) > 0]
    print(data)

# f = open("test.md", "w")
# f.write("Created file")