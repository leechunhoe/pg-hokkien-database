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
				content += "\n\n## 關係 관·희- Relationships"

				relations = {keyValue.split(":")[0] : keyValue.split(":")[1] for keyValue in member[0][6].split(".")}
				links = ""
				if "pa" in relations:
					links += "- [%s兮爸 Father](member%s.md)\n\n" %(hanji, relations["pa"])
				if "ma" in relations:
					links += "- [%s兮媽 Mother](member%s.md)\n\n" %(hanji, relations["ma"])
				if "ang" in relations:
					links += "- [%s兮翁 Husband](member%s.md)\n\n" %(hanji, relations["ang"])
				if "bo" in relations:
					links += "- [%s兮某 Wife](member%s.md)\n\n" %(hanji, relations["bo"])
				if "ko" in relations:
					links += "- [%s兮哥 Elder brother](member%s.md)\n\n" %(hanji, relations["ko"])
				if "ci" in relations:
					links += "- [%s兮姊 Elder sister](member%s.md)\n\n" %(hanji, relations["ci"])
				if "ti" in relations:
					links += "- [%s兮小弟 Younger brother](member%s.md)\n\n" %(hanji, relations["ti"])
				if "me" in relations:
					links += "- [%s兮小妹 Younger sister](member%s.md)\n\n" %(hanji, relations["moy"])
				if "hs1" in relations:
					links += "- [%s兮大漢後生 Elder son](member%s.md)\n\n" %(hanji, relations["hs1"])
				if "cw1" in relations:
					links += "- [%s兮大漢자와 Elder daughter](member%s.md)\n\n" %(hanji, relations["cw1"])
				if "hscw" in relations:
					links += "- [%s兮囝 Son/daughter](member%s.md)\n\n" %(hanji, relations["hscw"])
				if "hs" in relations:
					links += "- [%s兮後生 Son](member%s.md)\n\n" %(hanji, relations["hs"])
				if "cw" in relations:
					links += "- [%s兮자와 Daughter](member%s.md)\n\n" %(hanji, relations["cw"])
				if "hs2" in relations:
					links += "- [%s兮細漢後生 Younger son](member%s.md)\n\n" %(hanji, relations["hs2"])
				if "cw2" in relations:
					links += "- [%s兮細漢자와 Younger daughter](member%s.md)\n\n" %(hanji, relations["cw2"])
				content += "\n\n" + links

			content += "\n\n## 稱呼 칑·허· Namings"

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
