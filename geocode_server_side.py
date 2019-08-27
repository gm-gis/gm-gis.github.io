import urllib 
import requests
import json
import os 
from random import randrange
import pickle


workspace = 'C:\\Users\\Gregory\\Documents\\GitHub\\gm-gis.github.io'

with open(os.path.join(workspace,'contacts.json')) as f:
    contacts_json = json.load(f)
    # print(d[0])


coords_list = []

num_changed=0

failed_addresses = []

for count, record in enumerate(contacts_json):
	street = record['MailingStreet']
	city = record['MailingCity']
	state = record['MailingState']

	if count % 20 == 0:

		print("coding rec {} out of {}".format(count,len(contacts_json)))


	address="{},{},{}".format(street,city,state)
	key="AIzaSyD6SVUZkyXg1avnChyUwhDJoypvZkw6_LQ"
	url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, key)



	# Ping google for the reuslts:
	results = requests.get(url)
	# Results will be in JSON format - convert to dict using requests functionality
	results = results.json()

	# if there's no results or an error, return empty results.
	if len(results['results']) == 0:
			output = {
			    "formatted_address" : None,
			    "latitude": None,
			    "longitude": None,
			    "accuracy": None,
			    "google_place_id": None,
			    "type": None,
			    "postcode": None
			}
	else:    
	    answer = results['results'][0]
	    output = {
	        "formatted_address" : answer.get('formatted_address'),
	        "latitude": answer.get('geometry').get('location').get('lat'),
	        "longitude": answer.get('geometry').get('location').get('lng'),
	        "accuracy": answer.get('geometry').get('location_type'),
	        "google_place_id": answer.get("place_id"),
	        "type": ",".join(answer.get('types')),
	        "postcode": ",".join([x['long_name'] for x in answer.get('address_components') 
	                              if 'postal_code' in x.get('types')])
	    }


	coded_lon = output['longitude']
	coded_lat = output['latitude']

	if coded_lat and coded_lon: # check for non-null values

		coords_tuple = tuple([coded_lon,coded_lat])

		if coords_tuple not in coords_list:
			
			coords_list.append(coords_tuple)

			record['MailingLongitude'] = coded_lon
			record['MailingLatitude'] = coded_lat

		else:

			record['MailingLongitude'] = coded_lon + randrange(9)/1000
			record['MailingLatitude'] = coded_lat + randrange(9)/1000
			
			num_changed+=1

	else:

		failed_addresses.append(tuple([record["MailingStreet"],record['MailingCity'],record['MailingState'],record['MailingCountry']]))


jsonfile = open(os.path.join(workspace,'snarky_wombat.json'), 'w', encoding='utf-8')

jsonfile.write('contacts_list=')
jsonfile.close()

with open(os.path.join(workspace,'snarky_wombat.json'), 'a', encoding='utf-8') as jsonfile:
	jsonfile.write(str(contacts_json))
	# json.dump(d,jsonfile)

jsonfile.close()

second_json_file = open(os.path.join(workspace,'vanilla_widget.json'), 'w', encoding='utf-8')
second_json_file.write(str(contacts_json))
second_json_file.close()

out_pickle = open(os.path.join(workspace,"failed_addresses"), "wb")

pickle.dump(failed_addresses,out_pickle)

out_pickle.close()