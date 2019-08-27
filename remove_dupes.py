import urllib 
import requests
import json
import os 
from random import randrange


workspace = 'C:\\Users\\Gregory\\Documents\\GitHub\\gm-gis.github.io'

with open(os.path.join(workspace,'contacts_Pandas.json')) as f:
    contacts_json = json.load(f)


print(contacts_json[0]["MailingStreet"])

coords_list = []

num_changed=0

out_json = json.dumps(contacts_json)

jsonfile = open(os.path.join(workspace,'futuristic_hamburger.json'), 'w', encoding='utf-8')

jsonfile.write('contacts_list=')
jsonfile.close()

with open(os.path.join(workspace,'futuristic_hamburger.json'), 'a', encoding='utf-8') as jsonfile:
	jsonfile.write(out_json)

jsonfile.close()


print(num_changed)
	