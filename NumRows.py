import sys
import csv

filename = sys.argv[1]
file = open(filename)
try:
	
	length= sum(1 for row in file)
	print length
finally:
	file.close()

