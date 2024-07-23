import csv
from decimal import Decimal
import os
import os.path

from logic.Singleton import Singleton


class DataReader(metaclass=Singleton):
	def __init__(self):
		self._data = {}
	def _readCsv(self, filename: str) -> list[list[Decimal]]:	
		print(f'reading {filename}.csv')
		base_dir = os.getcwd()
		table = []
		with open(f'{base_dir}/csv/{filename}.csv') as csvfile:
			reader = csv.reader(csvfile)
			next(reader)
			next(reader)
			for row in reader:			
				table.append([Decimal(value) for value in row])
		#for row in table:
		#	print(row)
		return table
	def readCsv(self, filename:str):
		if filename in self._data:
			return self._data[filename]
		else:
			data = self._readCsv(filename)
			self._data[filename] = data
			return data

dr = DataReader()
def readSingleDataColumn(column, index : Decimal, csv_file: str):
	data =dr.readCsv(csv_file)
	for i in range(len(data)-1):
		if(data[i][0] <index < data[i+1][0]):
			return [(data[i][0], data[i][column]), (data[i+1][0], data[i+1][column])]
	print(f'panic in DataReader')
	return []
	
