import csv


def isBlank (myString):
    return not (myString and myString.strip())
#['ROW_ID', 'SUBJECT_ID', 'HADM_ID', 'ICUSTAY_ID', 'DBSOURCE', 'EVENTTYPE', 'PREV_CAREUNIT', 'CURR_CAREUNIT', 'PREV_WARDID', 'CURR_WARDID', 'INTIME', 'OUTTIME', 'LOS']

filer = open('TRANSFERS.csv')
filew = open('Transfer_table2.csv', 'wb')

try:
	inputnum = 0
	outputnum = 0
	reader = csv.DictReader(filer)
	reader.next()
	header = ['SUBJECT_ID', 'HADM_ID', 'DBSOURCE', 'EVENTTYPE', 'PREV_CAREUNIT', 'CURR_CAREUNIT', 'PREV_WARDID', 'CURR_WARDID', 'LOS',  'INTIME', 'OUTTIME']
	
	writer = csv.DictWriter(filew, fieldnames = header)
	writer.writeheader()
	for r in reader:
		inputnum = inputnum+1
		del r['ROW_ID']
		del r['ICUSTAY_ID']
		startpoint = r['INTIME']
		endpoint = r['OUTTIME']
		startpoint = startpoint[:4]+startpoint[5:7]+ startpoint[8:10]
		if(isBlank(startpoint)):
			
			print str(r['SUBJECT_ID']) + " is blank " + str(r['INTIME'])
			print r
			continue
		sp = int(startpoint)
		if isBlank(endpoint):
			continue  #removing discharge tuples
			#epinf = 'Inf'
			#r['INTIME'] = sp
			#r['OUTTIME'] = epinf
		else:
			endpoint = endpoint[:4]+endpoint[5:7]+endpoint[8:10]		
			ep = int(endpoint)
			if(ep-sp <= 0):
				print str(r['SUBJECT_ID']) + " wrong dates " + str(sp) + " , " +str(ep)
				continue
			r['INTIME'] = sp
			r['OUTTIME'] = ep
		writer.writerow(r)
		outputnum = outputnum +1
finally:
	filer.close()
	filew.close()
