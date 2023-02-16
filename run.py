#!/usr/bin/env python3
import os
import requests

"""
This script reads over text files with the description of the fruit and uploads these descriptions with the corresponding images 
"""

# define upload url
url = "http://localhost/fruits/"

# initialize empty dictionary
fruit_info = {}
    
# assign directory
directory = 'supplier-data/descriptions'
 
# iterate over files in that directory
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
        
    # separate filename from extension
    ff, e = os.path.splitext(filename)
    
    # ignore files that are not .txt
    if e != '.txt':
        continue
    
    # open each txt file and save the info in the dictionary then post it to the specified url
    with open(file) as f:
        lines = f.readlines()
        fruit_info["name"] = lines[0].strip('\n')
        fruit_info["weight"] = int(lines[1].split()[0])
        fruit_info["description"] = lines[2].strip('\n').strip('\xa0')
        fruit_info["image_name"] = ff + ".jpeg"
        print(fruit_info)
        
        response = requests.post(url, json=fruit_info)
        print(response.status_code)
        