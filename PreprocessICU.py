import csv

def isBlank (myString):
    return not (myString and myString.strip())

filer = open('ICUSTAYS.csv')
filew = open('ICUSTAYS_table.csv', 'wb')

try:
	inputnum = 0
	outputnum = 0
	reader = csv.DictReader(filer)
	reader.next(); #skiping fields name
	fieldsname = ['SUBJECT_ID', 'ICUSTAY_ID', 'DBSOURCE', 'FIRST_CAREUNIT', 'LAST_CAREUNIT', 'FIRST_WARDID', 'LAST_WARDID', 'LOS', 'INTIME', 'OUTTIME']
	writer = csv.DictWriter(filew, fieldnames = fieldsname)
        writer.writeheader()
	for r in reader:
		inputnum = inputnum +1
		del r['ROW_ID']
		del r['HADM_ID']
		startpoint = r['INTIME']
		endpoint = r['OUTTIME']
		startpoint = startpoint[:4]+startpoint[5:7]+ startpoint[8:10]
		sp = int(startpoint)
		if isBlank(endpoint):
			epinf = 'Inf'
			r['INTIME'] = sp
			r['OUTTIME'] = epinf
		else:
			endpoint = endpoint[:4]+endpoint[5:7]+endpoint[8:10]		
			ep = int(endpoint)
			if(ep-sp == 0):
				ep= ep+1
			r['INTIME'] = sp
			r['OUTTIME'] = ep
		writer.writerow(r)
		outputnum = outputnum +1
	print "number of rows in input file is " + str(inputnum)
	print "number of rows in output file is " + str(outputnum)

finally:
	filer.close()
	filew.close()
		
		
