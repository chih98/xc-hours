#!/usr/bin/env python
# © Marko Crnkovic, 2020 - www.mbobpro.com
# Goes through foreflight loogbook and
# returns all PIC XC hours.

filepath = input("Relative Path to ForeFlight's Logbook CSV: ")


try:
	file = open(filepath, 'r')
except (OSError, IOError):
	print("Path " + filepath + "threw an error. Try another file path.")
	exit(1)

entries = file.readlines()

# Skips aircraft lines. Starts calculating
# when "Date" is passed. 
# Will skip the next line though so
# we're not trying to cast the column
# titles as int's
start = False

totalXC = 0.0
totalPIC = 0.0
picXCTotal = 0.0


def safe_cast(val, to_type, default = None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


for line in entries:

	words = line.split(",")
	if words[0] == "Date":
		start = True

	if start != True:
		continue
	
	# Adding hour total
	pic = safe_cast(words[12], float, 0.0) # PIC is index 12
	xc = safe_cast(words[16], float, 0.0)  # XC is index 16
	
	totalXC += xc
	totalPIC += pic

	if xc > 0 and pic > 0:
		picXCTotal += float(xc)

totalXC = round(totalXC, 2)
totalPIC = round(totalPIC, 2)
picXCTotal = round(picXCTotal, 2)

print("======XC Totals======\n\nPIC:       " + safe_cast(totalPIC, str, "Unknown") +
	  "\nXC:        " + safe_cast(totalXC, str, "Unknown") +
	  "\nXC as PIC: "+ safe_cast(picXCTotal, str, "Unkonwn") +
	  "\n\n=====================")
