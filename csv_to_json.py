#csv_to_json

import csv
import json
import os

in_file=r'C:\\Users\\Gregory\\Documents\\alumni_connect\\Contact.csv'

data = []

os.chdir('C:\\Users\\Gregory\\Documents\\alumni_connect')
# with open(in_file, encoding = 'utf-8') as f:
#     for row in csv.DictReader(f):
#         data.append(row)

# json_data = json.dumps(data)


# out_json = open(r'C:\\Users\\Gregory\json.txt','wb')

# out_json.write(json_data)

csvfile = open('Contact.csv', 'r', encoding='utf-8')
jsonfile = open('Contacts.json', 'w', encoding='utf-8')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
csvfile.readline()
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')