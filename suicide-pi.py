import json
from pprint import pprint
import re



male_count = 0
female_count = 0

#key = age, value = number
males = {} 
females = {}
males["Under 18"] = 0
males["18-24"] = 0
males["25-34"] = 0
males["35-44"] = 0
males["Over 45"] = 0
females["Under 18"] = 0
females["18-24"] = 0
females["25-34"] = 0
females["35-44"] = 0
females["Over 45"] = 0

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

with open('deduped-data.json') as data_file:    
    data = json.load(data_file)
   
    for section in data:

    	isMale = 0
    	int_age = 0
        
        suicide = section['radio2']['The shooting was a suicide or suicide attempt.'].strip().lower()
        if 'yes' not in suicide:
        	continue

        gender = section['victim-section'][0]['gender'].lower().strip()
        if findWholeWord('male')(gender) is not None:
        	male_count += 1
        	isMale = 1

        if findWholeWord('female')(gender) is not None:
        	female_count += 1
        	isMale = 0

        age = section['victim-section'][0]['age']['value'].strip()
        age = age.replace(".","").replace(" ", "")
        age = re.sub('[^0-9]','', age)
        try:
        	int_age = int(age)
        except ValueError:
        	pass
        if int_age is not None:
        	if int(int_age) > 0 and int_age < 18:
	        	if isMale == 1:
	        		males["Under 18"] += 1
	        	elif isMale == 0:
	        		females["Under 18"] += 1
	        if int_age >= 18 and int_age < 25:
	        	if isMale == 1:
	        		males["18-24"] += 1
	        	else:
	        		females["18-24"] += 1
	        if int_age >= 25 and int_age < 35:
	        	if isMale == 1:
	        		males["25-34"] += 1
	        	else:
	        		females["25-34"] += 1
	        if int_age >= 35 and int_age < 45:
	        	if isMale == 1:
	        		males["35-44"] += 1
	        	else:
	        		females["35-44"] += 1
	        if int_age >= 45:
	        	if isMale == 1:
	        		males["Over 45"] += 1
	        	else:
	        		females["Over 45"] += 1

for key, value in males.items():
	print '[', key, ',', value, ']'
for key, value in females.items():
	print '[', key, ',', value, ']'

