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

			if len(member[0]) > 6:
				relations = {keyValue.split(":")[0] : keyValue.split(":")[1] for keyValue in member[0][6].split(".")}
				links = ""
				if relations["pa"] != "-1":
					links += "[%s兮爸 Father](member%s.md)\t" %(hanji, relations["pa"])
				if relations["ma"] != "-1":
					links += "[%s兮媽 Mother](member%s.md)\n\n" %(hanji, relations["ma"])
				if relations["an"] != "-1":
					links += "[%s兮翁 Husband](member%s.md)\t" %(hanji, relations["an"])
				if relations["bo"] != "-1":
					links += "[%s兮某 Wife](member%s.md)\n\n" %(hanji, relations["bo"])
				if relations["ko"] != "-1":
					links += "[%s兮哥 Elder brother](member%s.md)\t" %(hanji, relations["ko"])
				if relations["ci"] != "-1":
					links += "[%s兮姊 Elder sister](member%s.md)\n\n" %(hanji, relations["ci"])
				if relations["ti"] != "-1":
					links += "[%s兮小弟 Younger brother](member%s.md)\t" %(hanji, relations["ti"])
				if relations["me"] != "-1":
					links += "[%s兮小妹 Younger sister](member%s.md)\n\n" %(hanji, relations["me"])
				if relations["hs"] != "-1":
					links += "[%s兮囝 Son](member%s.md)\t" %(hanji, relations["hs"])
				if relations["cw"] != "-1":
					links += "[%s兮자와 Daughter](member%s.md)\n\n" %(hanji, relations["cw"])
				if relations["hs2"] != "-1":
					links += "[%s兮細漢囝 Younger son](member%s.md)\t" %(hanji, relations["hs2"])
				if relations["cw2"] != "-1":
					links += "[%s兮細漢자와 Younger daughter](member%s.md)\n\n" %(hanji, relations["cw2"])
				content += "\n\n" + links

			tables = ""
			for variant in member:
				tables += "漢字/諺文 | %s\n" %variant[1]
				tables += "--- | ---\n"
				tables += "諺文 깐-뿐ˆ | %s\n" %variant[2]
				tables += "台羅 Tâi-lô | %s\n" %variant[3]
				tables += "戴字 Taiji | %s\n" %variant[4]
				tables += "\n\n"
			content += "\n\n" + tables

			f.write(content)

main()
