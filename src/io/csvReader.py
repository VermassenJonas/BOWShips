import csv

with open('test.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		print(' - '.join(row))
