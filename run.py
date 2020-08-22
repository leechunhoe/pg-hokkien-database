import csv
import numpy as np
from itertools import groupby

def main():
	members = get_members()
	relations = get_relations()
	generate_linked_member_files(members, relations)
	generate_index(members)

def get_members():
	data = get_csv_entries("data.csv")
	return [list(i) for j, i in groupby(data, lambda a: a[0])]

def get_relations():
	return get_csv_entries("relation.csv")

def get_relation(relations, key):
	return [r for r in relations if r[0] == key][0]

def get_csv_entries(filename):
	content = read_csv(filename)
	return [row for row in content if len(row) > 0]

def read_csv(filename):
	file = open(filename, "r")
	return csv.reader(file, delimiter=',')

def generate_linked_member_files(members, relationships):
	# Generate linked member files
	for member in members:
		id = member[0][0]
		f = open("members/member%s.md" %id, "w")
		content = ""

		hanji = member[0][1]
		english = member[0][5].capitalize()

		# # Populate his/her relationship with me
		my_relation = ""
		if len(member[0]) > 7:
			relations_text = member[0][7]
			relations = relations_text.split(".")
			my_relation_list = []

			me_link = "[%s](%s)"%("我", "member1.md")
			my_relation_list.append(me_link)

			for i, relation in enumerate(relations):
				# 1. Get data
				relation_code = relation.split(":")[1] # relationship code, e.g. "pa", "ma"
				relationship = get_relation(relationships, relation_code)
				this_hanji = relationship[1]

				# 2. Append
				if i == len(relations) - 1:
					my_relation_list.append(this_hanji)
				else:
					member_id = relations[i + 1].split(":")[0] # the member instance (integer)
					filename = "member%s.md" %member_id
					this_link = "[%s](%s)"%(this_hanji, filename)
					my_relation_list.append(this_link)

			my_relation = " 兮 ".join(my_relation_list)

		title = "# %s\n## 가我兮關係\n\n%s _%s_" %(hanji, my_relation, english)
		content += title

		english_possessive = "%s's" %english
		if id == "1":
			english_possessive = "My"

		# Populate his/her direct relationships
		if len(member[0]) > 6:
			content += "\n\n## 關係 관·희- _Relationships_"

			relations_text = member[0][6]

			if len(relations_text) > 0:
				# TODO Refactor
				relations = {keyValue.split(":")[0] : keyValue.split(":")[1] for keyValue in relations_text.split(".")}
				links = ""

				for relationship in relationships:
					if relationship[0] in relations:
						links += get_link(relationship[1], relationship[2], hanji, english_possessive, relations[relationship[0]], members)

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
