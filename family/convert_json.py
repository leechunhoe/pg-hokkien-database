import csv
import numpy as np
from itertools import groupby
import json

def main():
	members = get_members()
	members_json = []
	for member in members:
		variant_main = member[0]
		member_json = {
			"id": variant_main[0],
			"english": variant_main[5],
			"his_relations": get_his_relations(variant_main),
			"my_relations": get_my_relations(variant_main),
			"variants": get_variants(member)
		}
		members_json.append(member_json)

def get_variants(member):
	variants = []
	for variant in member:
		variant_json = {
			"hanji": variant[1],
			"imji": variant[2],
			"tailo": variant[3],
			"taiji": variant[4]
		}
		variants.append(variant_json)
	return variants

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