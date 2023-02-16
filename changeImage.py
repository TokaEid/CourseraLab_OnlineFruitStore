#!/usr/bin/env python3

import os
from PIL import Image

"""
This script takes images that are .tiff, resizes them then converts them to .jpeg
"""


# assign directory
directory = 'supplier-data/images'
 
# iterate over files in that directory
for filename in os.listdir(directory):
    image = os.path.join(directory, filename)
    
    # separate filename from extension
    f, e = os.path.splitext(filename)
    
    # ignore files that are not .tiff 
    if e !=  '.tiff':
        continue
        
    # define new image name with .jpeg extension
    new_im_name = "supplier-data/images/" + f + '.jpeg'
    
    # open image, change size and convert to RGB
    im = Image.open(image)    
    new_im = im.resize((600,400)).convert('RGB')
    
    # save new image as JPEG
    new_im.save(new_im_name, 'JPEG')