#!/usr/bin/env python3
import os
import requests

"""
This script uploads jpeg images to the specified url
"""

# define upload url
url = "http://localhost/upload/"
    
# assign directory
directory = 'supplier-data/images'
 
# iterate over files in that directory
for filename in os.listdir(directory):
    image = os.path.join(directory, filename)
        
    # separate filename from extension
    f, e = os.path.splitext(filename)
    
    # ignore files that are not .jpeg
    if e != '.jpeg':
        continue
    
    # open each image and post it to url
    with open(image, rb) as opened:
        r = requests.post(url, files={'file': opened})
