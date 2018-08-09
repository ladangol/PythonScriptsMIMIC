import csv

file = open('Prescriptions_table.csv')
filew = open('Preschunk15m.csv', 'wb')
try:
	reader = csv.reader(file)
	writer = csv.writer(filew)
	row_num = 0
	for row in reader:
		row_num = row_num+1
		if(row_num == 1500000):
			break
		else:
			writer.writerow(row)
		

finally:
	file.close()
