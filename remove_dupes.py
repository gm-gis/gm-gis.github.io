import urllib 
import requests
import json
import os 
from random import randrange


workspace = 'C:\\Users\\Gregory\\Documents\\GitHub\\gm-gis.github.io'

with open(os.path.join(workspace,'geocoded_read.json'),encoding="utf8") as f:
    contacts_json = json.load(f)


coords_list = []

num_changed=0

for count, record in enumerate(contacts_json):
	coords_tuple = tuple(record['MailingLongitude'],record['MailingLatitude'])
	if coords_tuple not in coords_list:
		coords_list.append(coords_tuple)
	else:
		record['MailingLongitude'] += randrange(9)/1000
		record['MailingLatitude'] += randrange(9)/1000
		num_changed+=1


jsonfile = open(os.path.join(workspace,'futuristic_hamburger.json'), 'w', encoding='utf-8')

jsonfile.write('contacts_list=')
jsonfile.close()

with open(os.path.join(workspace,'futuristic_hamburger.json'), 'a', encoding='utf-8') as jsonfile:
	jsonfile.write(str(contacts_json))

jsonfile.close()


print(num_changed)
	