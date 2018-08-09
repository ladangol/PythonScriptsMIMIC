import csv

def isBlank (myString):
    return not (myString and myString.strip())

filer = open('PRESCRIPTIONS.csv')
filew = open('Prescriptions_table.csv', 'wb')


try:
	infnum =0
	wrongdatenum = 0
        startpointblank = 0
	inputnum = 0
	outputnum = 0
	reader = csv.DictReader(filer)
	reader.next(); #skiping fields name
	fieldsname = ['SUBJECT_ID', 'DRUG_TYPE', 'DRUG', 'FORMULARY_DRUG_CD', 'GSN', 'NDC', 'PROD_STRENGTH', 'DOSE_VAL_RX', 'DOSE_UNIT_RX', 'FORM_VAL_DISP', 'FORM_UNIT_DISP', 'ROUTE', 'STARTDATE', 'ENDDATE']
	writer = csv.DictWriter(filew, fieldnames = fieldsname)
        writer.writeheader()
	for r in reader:
		inputnum = inputnum +1
		del r['ROW_ID']
		del r['HADM_ID']
		del r['ICUSTAY_ID']
		del r['DRUG_NAME_POE']
		del r['DRUG_NAME_GENERIC']
		startpoint = r['STARTDATE']
		endpoint = r['ENDDATE']
		startpoint = startpoint[:4]+startpoint[5:7]+ startpoint[8:10]
		if(isBlank(startpoint)):
			startpointblank = startpointblank +1
			continue
		sp = int(startpoint)
		if isBlank(endpoint):
			infnum = infnum+1
			epinf = 'Inf'
			r['STARTDATE'] = sp
			r['ENDDATE'] = epinf
		else:
			endpoint = endpoint[:4]+endpoint[5:7]+endpoint[8:10]		
			ep = int(endpoint)
			if(ep-sp < 0):
				wrongdatenum = wrongdatenum+1
			if(ep-sp <= 0):
				continue
			r['STARTDATE'] = sp
			r['ENDDATE'] = ep
		writer.writerow(r)
		outputnum = outputnum +1
	print "number of rows in input file is " + str(inputnum)
	print "number of rows in output file is " + str(outputnum)
	print "number of startpoint is blank records is "+ str(startpointblank)
	print "start point < end point " + str(wrongdatenum)
	print "Replaced endpoint with inf" + str(infnum)

finally:
	filer.close()
	filew.close()
		
		
