import csv

def isBlank (myString):
    return not (myString and myString.strip())

filer = open('ADMISSIONS.csv')
filew = open('admission_table.csv', 'wb')

try:
	inputnum = 0
	outputnum = 0
	reader = csv.DictReader(filer)
	reader.next(); #skiping fields name
	header = ['SUBJECT_ID', 'ADMISSION_TYPE', 'ADMISSION_LOCATION', 'DISCHARGE_LOCATION', 'INSURANCE', 'LANGUAGE', 'RELIGION', 'MARITAL_STATUS', 'ADMITTIME', 'DISCHTIME']
	writer = csv.DictWriter(filew, fieldnames = header)
        writer.writeheader()
	for r in reader:
		inputnum = inputnum +1
		del r['ROW_ID']
		del r['HADM_ID']
		del r['EDREGTIME']
		del r['EDOUTTIME']
		del r['HOSPITAL_EXPIRE_FLAG']
		del r['HAS_CHARTEVENTS_DATA']
		del r['DIAGNOSIS']
		del r['ETHNICITY']
		del r['DEATHTIME']
		startpoint = r['ADMITTIME']
		endpoint = r['DISCHTIME']
		startpoint = startpoint[:4]+startpoint[5:7]+ startpoint[8:10]
		sp = int(startpoint)
		if isBlank(endpoint):
			epinf = 'Inf'
			r['ADMITTIME'] = sp
			r['DISCHTIME'] = epinf
		else:
			endpoint = endpoint[:4]+endpoint[5:7]+endpoint[8:10]		
			ep = int(endpoint)
			if (ep-sp > 0):
				r['ADMITTIME'] = sp
				r['DISCHTIME'] = ep
			else:
				continue		
		writer.writerow(r)
		outputnum = outputnum +1
	print "number of rows in input file is " + str(inputnum)
	print "number of rows in output file is " + str(outputnum)

finally:
	filer.close()
	filew.close()
		
		
