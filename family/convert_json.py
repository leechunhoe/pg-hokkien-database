import csv
import numpy as np
from itertools import groupby

def main():
	members = get_members()
	print(members)

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