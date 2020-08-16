import csv
from itertools import groupby

def main():
	with open('data.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		data = [row for row in csv_reader if len(row) > 0]
		members = [list(i) for j, i in groupby(data, lambda a: a[0])]

		for member in members:
			id = member[0][0]
			f = open("members/member%s.md" %id, "w")
			content = ""

			hanji = member[0][1].capitalize()
			english = member[0][5].capitalize()

			title = "# %s %s" %(hanji, english)
			content += title

			english_possessive = "%s's" %english
			if id == "0":
				english_possessive = "My"

			if len(member[0]) > 6:
				content += "\n\n## 關係 관·희- Relationships"

				relations = {keyValue.split(":")[0] : keyValue.split(":")[1] for keyValue in member[0][6].split(".")}
				links = ""
				if "pa" in relations:
					links += "- [%s兮爸 %s father](member%s.md)\n\n" %(hanji, english_possessive, relations["pa"])
				if "ma" in relations:
					links += "- [%s兮媽 %s mother](member%s.md)\n\n" %(hanji, english_possessive, relations["ma"])
				if "ang" in relations:
					links += "- [%s兮翁 %s husband](member%s.md)\n\n" %(hanji, english_possessive, relations["ang"])
				if "bo" in relations:
					links += "- [%s兮某 %s wife](member%s.md)\n\n" %(hanji, english_possessive, relations["bo"])
				if "ht" in relations:
					links += "- [%s兮兄弟 %s brother](member%s.md)\n\n" %(hanji, english_possessive, relations["ht"])
				if "ko" in relations:
					links += "- [%s兮哥 %s elder brother](member%s.md)\n\n" %(hanji, english_possessive, relations["ko"])
				if "ti" in relations:
					links += "- [%s兮小弟 %s younger brother](member%s.md)\n\n" %(hanji, english_possessive, relations["ti"])
				if "cm" in relations:
					links += "- [%s兮姊妹 %s sister](member%s.md)\n\n" %(hanji, english_possessive, relations["cm"])
				if "ci" in relations:
					links += "- [%s兮姊 %s elder sister](member%s.md)\n\n" %(hanji, english_possessive, relations["ci"])
				if "moy" in relations:
					links += "- [%s兮小妹 %s younger sister](member%s.md)\n\n" %(hanji, english_possessive, relations["moy"])
				if "hs1" in relations:
					links += "- [%s兮大漢後生 %s elder son](member%s.md)\n\n" %(hanji, english_possessive, relations["hs1"])
				if "cw1" in relations:
					links += "- [%s兮大漢자와 %s elder daughter](member%s.md)\n\n" %(hanji, english_possessive, relations["cw1"])
				if "hscw" in relations:
					links += "- [%s兮囝 %s children](member%s.md)\n\n" %(hanji, english_possessive, relations["hscw"])
				if "hs" in relations:
					links += "- [%s兮後生 %s son](member%s.md)\n\n" %(hanji, english_possessive, relations["hs"])
				if "cw" in relations:
					links += "- [%s兮자와 %s daughter](member%s.md)\n\n" %(hanji, english_possessive, relations["cw"])
				if "hs2" in relations:
					links += "- [%s兮細漢後生 %s younger son](member%s.md)\n\n" %(hanji, english_possessive, relations["hs2"])
				if "cw2" in relations:
					links += "- [%s兮細漢자와 %s younger daughter](member%s.md)\n\n" %(hanji, english_possessive, relations["cw2"])
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
