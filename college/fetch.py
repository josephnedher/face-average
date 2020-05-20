#!/usr/bin/env python
import requests
import os
import sys
adm=sys.argv[1:]

image_url = "http://elive.sjcetpalai.ac.in/Uploads/Admission/"
image_set=[]
for xval in adm:
    yval=image_url+xval+".jpg"
    image_set.append(yval)


for img in image_set:
 file_name = img.split('/')[-1]
 print("Downloading file:%s"%file_name)
 r = requests.get(img, stream=True)
 # this should be file_name variable instead of "file_name" string
 with open(os.path.join('/Downloads/college/images/',file_name), 'wb') as f:
    for chunk in r:
       f.write(chunk)
