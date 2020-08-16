import csv
from itertools import groupby



with open('data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	data = [row for row in csv_reader if len(row) > 0]
	members = [list(i) for j, i in groupby(data, lambda a: a[0])]
	for member in members:
		id = member[0][0]
		english = member[0][5]
		f = open("member%s.md" %id, "w")
		title = "# %s" %english

		tables = ""
		# TODO Add tables
		for variant in member:
			tables += "漢字/諺文 | %s\n" %variant[1]
			tables += "--- | ---\n"
			tables += "諺文 깐-뿐ˆ | %s\n" %variant[2]
			tables += "台羅 Tâi-lô | %s\n" %variant[3]
			tables += "戴字 Taiji | %s\n" %variant[4]

		# TODO Add links

		content = title + "\n\n" + tables

		f.write(content)