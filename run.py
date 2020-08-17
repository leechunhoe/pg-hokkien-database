import csv
import numpy as np
from itertools import groupby

def main():
	with open('data.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		data = [row for row in csv_reader if len(row) > 0]
		members = [list(i) for j, i in groupby(data, lambda a: a[0])]

		generate_linked_member_files(members)
		generate_index(members)

def generate_linked_member_files(members):
	# Generate linked member files
	for member in members:
		id = member[0][0]
		f = open("members/member%s.md" %id, "w")
		content = ""

		hanji = member[0][1]
		english = member[0][5].capitalize()

		title = "# %s\n%s" %(hanji, english)
		content += title

		english_possessive = "%s's" %english
		if id == "1":
			english_possessive = "My"

		if len(member[0]) > 6:
			content += "\n\n## 關係 관·희- _Relationships_"

			relations = {keyValue.split(":")[0] : keyValue.split(":")[1] for keyValue in member[0][6].split(".")}
			links = ""
			if "pa" in relations:
				links += get_link("爸", "father", hanji, english_possessive, relations["pa"], members)
			if "ma" in relations:
				links += get_link("媽", "mother", hanji, english_possessive, relations["ma"], members)
			if "ang" in relations:
				links += get_link("尪", "husband", hanji, english_possessive, relations["ang"], members)
			if "bo" in relations:
				links += get_link("某", "wife", hanji, english_possessive, relations["bo"], members)
			if "ht" in relations:
				links += get_link("兄弟", "brother", hanji, english_possessive, relations["ht"], members)
			if "ko" in relations:
				links += get_link("哥", "elder brother", hanji, english_possessive, relations["ko"], members)
			if "ti" in relations:
				links += get_link("小弟", "younger brother", hanji, english_possessive, relations["ti"], members)
			if "cm" in relations:
				links += get_link("姊妹", "sister", hanji, english_possessive, relations["cm"], members)
			if "ci" in relations:
				links += get_link("姊", "elder sister", hanji, english_possessive, relations["ci"], members)
			if "moy" in relations:
				links += get_link("小妹", "younger sister", hanji, english_possessive, relations["moy"], members)
			if "hs1" in relations:
				links += get_link("大漢後生", "elder son", hanji, english_possessive, relations["hs1"], members)
			if "cw1" in relations:
				links += get_link("大漢자와", "elder daughter", hanji, english_possessive, relations["cw1"], members)
			if "hscw" in relations:
				links += get_link("囝", "children", hanji, english_possessive, relations["hscw"], members)
			if "hs" in relations:
				links += get_link("後生", "son", hanji, english_possessive, relations["hs"], members)
			if "cw" in relations:
				links += get_link("자와", "daughter", hanji, english_possessive, relations["cw"], members)
			if "hs2" in relations:
				links += get_link("細漢後生", "younger son", hanji, english_possessive, relations["hs2"], members)
			if "cw2" in relations:
				links += get_link("細漢자와", "younger daughter", hanji, english_possessive, relations["cw2"], members)
			content += "\n\n" + links

		content += "\n\n## 稱呼 칑·허· _Address_"

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

def get_link(hanji_title, english_title, hanji, english_possessive, relation, members):
	member = [m for m in members if m[0][0] == relation][0][0][1]
	return "- [%s兮%s (%s) %s %s](member%s.md)\n\n" %(hanji, hanji_title, member, english_possessive, english_title, relation)

def generate_index(members):
	f = open("README.md", "w")
	content = "# 家庭 Family\n\n"
	content += "漢字/諺文 | English\n"
	content += "--- | ---\n"
	for member in members:
		id = member[0][0]
		hanji = member[0][1].capitalize()
		english = member[0][5].capitalize()
		filename = "members/member%s.md" %id
		content += "[%s](%s) | [%s](%s)\n" %(hanji, filename, english, filename)

	f.write(content)

main()
