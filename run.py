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
		content = get_member_content(relationships, members, member)
		f.write(content)

def get_member_content(relationships, members, member):
	id = member[0][0]
	content = ""
	content += get_my_relations_content(relationships, members, member)
	content += get_his_relations_content(relationships, members, member)
	content += get_address_content(member)
	return content

def get_his_relations_content(relationships, members, member):
	id = member[0][0]
	content = ""

	hanji = member[0][1]
	english = member[0][5].capitalize()

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
					links += get_his_relation(relationship[1], relationship[2], hanji, english_possessive, relations[relationship[0]], members)

			content += "\n\n" + links
	return content

def get_my_relations_content(relationships, members, member):
	hanji = member[0][1]
	english = member[0][5].capitalize()

	# Populate his/her relationship with me
	my_full_relation = ""
	my_quick_relation = ""
	if len(member[0]) > 7:
		relations_text = member[0][7]
		relations = relations_text.split(".")
		my_full_relation = "詳：%s"%get_my_full_relation(members, relationships, relations)
		my_quick_relation = "簡：%s"%get_my_quick_relation(members, relationships, relations)

	return "# %s\n## 定義 딍-끼- _Definition_\n%s\n\n%s\n\n英：%s" %(hanji, my_quick_relation, my_full_relation, english)

def get_address_content(member):
	content = "\n\n## 稱呼 칑·허· _Address_"
	content += "\n\n" + get_name_tables(member)
	return content

def get_name_tables(member):
	tables = ""
	for variant in member:
		tables += "漢字/諺文 | %s\n" %variant[1]
		tables += "--- | ---\n"
		tables += "諺文 깐-뿐ˆ | %s\n" %variant[2]
		tables += "台羅 Tâi-lô | %s\n" %variant[3]
		tables += "戴字 Taiji | %s\n" %variant[4]
		tables += "\n\n"
	return tables

# e.g. 我兮爸兮爸兮哥
# members: from data.csv
# relationships: from relation.csv
# relations: relation chain from me e.g. pa:1.ma:2
def get_my_full_relation(members, relationships, relations):
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

	return " 兮 ".join(my_relation_list)

# e.g. 阿公兮哥
# members: from data.csv
# relationships: from relation.csv
# relations: relation chain from me e.g. 1:pa.2:ma
def get_my_quick_relation(members, relationships, relations):
	# Part 2: Get quick relation
	relation = relations[-1]
	last_member_id = relation.split(":")[0] # the member instance (integer)
	last_relation_code = relation.split(":")[1] # relationship code, e.g. "pa", "ma"
	last_member_hanji = get_member_primary(members, last_member_id)[1]
	relation_hanji = get_relation(relationships, last_relation_code)[1]
	return "[%s](member%s.md) 兮 %s"% (last_member_hanji, last_member_id, relation_hanji)

def get_his_relation(hanji_title, english_title, hanji, english_possessive, relation, members):
	member_hanji = get_member_primary(members, relation)[1]
	return "- %s 兮 [%s → %s](member%s.md) %s %s\n\n" %(hanji, hanji_title, member_hanji, relation, english_possessive, english_title)

# Get the primary entry of member
def get_member_primary(members, member_id):
	return get_member(members, member_id)[0]

# Get the all entries of member
def get_member(members, member_id):
	return [m for m in members if m[0][0] == member_id][0]

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
