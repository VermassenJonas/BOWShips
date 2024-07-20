import csv
from decimal import Decimal
import os
base_dir = os.getcwd()
print(base_dir)
def readCsv() -> list[list[Decimal]]:
	table = []
	with open(f'{base_dir}/csv/default/engineWeight.csv') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		next(reader)
		for row in reader:			
			table.append([Decimal(value) for value in row])
	for row in table:
		print(row)
	return table
readCsv()

input('done')