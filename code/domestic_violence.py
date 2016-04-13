import json
from pprint import pprint

with open('deduped-data.json') as data_file:    
    data = json.load(data_file)

def hasNumbers(inputString):
  return any(char.isdigit() for char in inputString)

for section in data:
	if section['radio1']['The incident was a case of domestic violence.'].strip() != "":
		d = section['radio1']['The incident was a case of domestic violence.'].strip()
		if "Yes" in d:
			for entry in section['victim-section']:
				if entry['gender'] != "" and entry['age'] != '' and entry['age'] != '\n':
					age = entry['age']['value'].strip()
					print entry['gender'], '\t', age

