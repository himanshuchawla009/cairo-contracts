# Python program to read
# json file
 
 
import json
 
# Opening JSON file
f = open('account_compiled.json', 'r+')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
str_data = []
for i in data['program']['data']:
    a = str(i)
    str_data.append(a)

print(str_data)
data['program']['data'] = str_data
f.write(json.dumps(data))
# Closing file
f.close()