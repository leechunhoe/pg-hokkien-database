import csv
import numpy as np
from itertools import groupby
import json

def main():
	members = get_members()
	members_json = []
	for member in members:
		variant_main = member[0]

		his_relations = get_his_relations(variant_main)
		my_relations = get_my_relations(variant_main)

		member_json = {
			"id": variant_main[0],
			"english": variant_main[5],
			"his_relations": his_relations,
			"my_relations": my_relations
		}
		members_json.append(member_json)

	print(members_json)

def get_his_relations(variant_main):
	raw_string = get_item_if_exist(variant_main, 6)
	if (raw_string == None or len(raw_string) == 0):
		return {}

	result = {}
	for relation in raw_string.split("."):
		key = relation.split(":")[0]
		value = relation.split(":")[1]
		result[key] = value

	return result

def get_my_relations(variant_main):
	raw_string = get_item_if_exist(variant_main, 7)
	if (raw_string == None or len(raw_string) == 0):
		return {}

	result = []
	for relation in raw_string.split("."):
		key = relation.split(":")[0]
		value = relation.split(":")[1]
		result.append({key: value})

	return result

def get_item_if_exist(list, index):
	if (len(list) > index):
		return list[index]
	else:
		return None

def get_members():
	data = get_csv_entries("data.csv")
	return [list(i) for j, i in groupby(data, lambda a: a[0])]

def get_csv_entries(filename):
	content = read_csv(filename)
	return [row for row in content if len(row) > 0]

def read_csv(filename):
	file = open(filename, "r")
	return csv.reader(file, delimiter=',')

main()