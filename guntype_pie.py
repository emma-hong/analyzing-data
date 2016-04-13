import json
from pprint import pprint

with open('deduped-data.json') as data_file:    
    data = json.load(data_file)

fatal_hg_count = 0
fatal_lg_count = 0
fatal_mg_count = 0
nf_hg_count = 0
nf_lg_count = 0
nf_mg_count = 0

for section in data:
	gun_type = ''
	victim_was = "nonfatal"
	if section['circumstances']['type-of-gun']['value'].strip() != "":
		d = section['circumstances']['type-of-gun']['value'].strip()
		#print d
		if "machine gun" in d or "assault rifle" in d or 'AR-15' in d or 'AK-47' in d: 
			gun_type = "machine gun"
		elif "handgun" in d or "pistol" in d or "revolver" in d: 
			gun_type = "handgun"
		elif "long gun" in d or "rifle" in d or "shotgun" in d:
			gun_type = "long gun"
		
	for d in section['victim-section']:
		if 'killed' in d['victim-was']:
			fatal = "fatal"
			if gun_type == "handgun":
				fatal_hg_count += 1
			elif gun_type == "long gun":
				fatal_lg_count += 1
			elif gun_type == "machine gun":
				fatal_mg_count += 1 
		else:
			if gun_type == "handgun":
				nf_hg_count += 1
			elif gun_type == "long gun":
				nf_lg_count += 1
			elif gun_type == "machine gun":
				nf_mg_count += 1 

print "fatal", '\n', "hg:", fatal_hg_count, "lg:", fatal_lg_count, "mg:", fatal_mg_count
print '\n', "nonfatal", "hg:", nf_hg_count, "lg:", nf_lg_count, "mg:", nf_mg_count
