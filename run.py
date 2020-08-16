import csv
from itertools import groupby

def main():
	with open('data.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		data = [row for row in csv_reader if len(row) > 0]
		members = [list(i) for j, i in groupby(data, lambda a: a[0])]

		for member in members:
			id = member[0][0]
			f = open("member%s.md" %id, "w")
			content = ""

			hanji = member[0][1].capitalize()
			english = member[0][5].capitalize()

			title = "# %s %s" %(hanji, english)
			content += title

			tables = ""
			for variant in member:
				tables += "漢字/諺文 | %s\n" %variant[1]
				tables += "--- | ---\n"
				tables += "諺文 깐-뿐ˆ | %s\n" %variant[2]
				tables += "台羅 Tâi-lô | %s\n" %variant[3]
				tables += "戴字 Taiji | %s\n" %variant[4]
				tables += "\n\n"
			content += "\n\n" + tables

			# TODO Add links
			if len(member[0]) > 6:
				relations = {keyValue.split(":")[0] : keyValue.split(":")[1] for keyValue in member[0][6].split(".")}
				links = ""
				if relations["pa"] != "-1":
					links += "[父 Father](member%s.md)\t" %relations["pa"]
				if relations["ma"] != "-1":
					links += "[母 Mother](member%s.md)\n\n" %relations["ma"]
				if relations["an"] != "-1":
					links += "[尪 Husband](member%s.md)\t" %relations["an"]
				if relations["bo"] != "-1":
					links += "[某 Wife](member%s.md)\n\n" %relations["bo"]
				if relations["ko"] != "-1":
					links += "[兄 Elder brother](member%s.md)\t" %relations["ko"]
				if relations["ci"] != "-1":
					links += "[姊 Elder sister](member%s.md)\n\n" %relations["ci"]
				if relations["ti"] != "-1":
					links += "[弟 Younger brother](member%s.md)\t" %relations["ti"]
				if relations["me"] != "-1":
					links += "[妹 Younger sister](member%s.md)\n\n" %relations["me"]
				if relations["hs"] != "-1":
					links += "[囝 Son](member%s.md)\t" %relations["hs"]
				if relations["cw"] != "-1":
					links += "[자와 Daughter](member%s.md)\n\n" %relations["cw"]
				content += "\n\n" + links

			f.write(content)

main()
