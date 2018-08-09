import csv

p = 61   #change as you wish
file = open('PRESch20_table.csv')
filep = open('PRESPatient'+str(p)+'.csv', 'wb')

try:
	reader =csv.DictReader(file)
	reader.next()
	fieldsname = ['SUBJECT_ID', 'DRUG_TYPE', 'DRUG', 'FORMULARY_DRUG_CD', 'GSN', 'NDC', 'PROD_STRENGTH', 'DOSE_VAL_RX', 'DOSE_UNIT_RX', 'FORM_VAL_DISP', 'FORM_UNIT_DISP', 'ROUTE', 'STARTDATE', 'ENDDATE']
	writer = csv.DictWriter(filep, fieldnames = fieldsname)
	writer.writeheader()
	for row in reader:
		if (row['SUBJECT_ID'] == str(p)):
			writer.writerow(row) 
finally:
	file.close()
	filep.close()
