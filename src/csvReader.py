import csv

with open('csv/default/engineWeight.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		print(' - '.join(row))

