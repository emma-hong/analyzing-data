import json
from pprint import pprint
import re
with open('deduped-data.json') as data_file:    
    data = json.load(data_file)

fatal= 0
nonfatal = 0
time_fatal = {}
time_nonfatal = {}
for count in range(0,25):
	if count not in time_fatal:
		time_fatal[count] = 0
	if count not in time_nonfatal:
		time_nonfatal[count] = 0

for section in data:
	victim_was = "nonfatal"
	hour = 0
	night = 0
	morning = 0
	time = section['date-and-time']['clock-time']['value'].strip()
	time = str(time)
	if 'pm' in time or 'p.m.' in time or 'PM' in time or 'P.M.' in time:
		night = 1
		morning = 0
		#print "NIGHT"
	if 'am' in time or 'a.m.' in time or 'AM' in time or 'A.M.' in time:
		morning = 1
		night = 0
		#print "MORNING"
	time = time.replace(".","")
	time = time.replace(" ", "").split(":")[0]
	time = re.sub('[^0-9]','', time)
	if night == 1 and morning == 0:
		try:
			time = int(time)
			hour = time + 12
		except ValueError:
			pass
	elif morning == 1 and night == 0:
		try:
			time = int(time)
			hour = time
		except ValueError:
			pass
	
	for d in section['victim-section']:
		if 'killed' in d['victim-was']:
			fatal += 1
			if not hour < 1 and not hour > 24:
				time_fatal[hour] += 1
		else:
			nonfatal +=1
			if not hour < 1 and not hour > 24:
				time_nonfatal[hour] += 1
#print "fatal: ", '\n', time_fatal
#print "nonfatal: ", '\n', time_nonfatal

for count in range(0,25):
	print '[', count, ',' ,time_fatal[count], ',' ,time_nonfatal[count], ']',','
