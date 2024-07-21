import csv
from decimal import Decimal
import os
import os.path



def readCsv() -> list[list[Decimal]]:	
	base_dir = os.getcwd()
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