#csv_to_json

import csv
import json
import os
import pandas as pd 

in_file=r'C:\\Users\\Gregory\\Documents\\alumni_connect\\Contact.csv'

data = []

os.chdir('C:\\Users\\Gregory\\Documents\\alumni_connect')

csvfile = open('Contact.csv', 'r', encoding='utf-8')
jsonfile = open('Contacts_pandas.json', 'w', encoding='utf-8')

df = pd.read_csv('Contact.csv')
out_json = df.to_json(orient='records')

jsonfile.write('contacts_list=')
jsonfile.close()

jsonfile = open('Contacts_pandas.json', 'a', encoding='utf-8')
jsonfile.write(out_json)
jsonfile.close()