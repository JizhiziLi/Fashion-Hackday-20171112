###########
# Created by Jizhizi Li @ 31/10/2017
# A simple download function to download images and texts
# after crawling from Iconic website (https://www.theiconic.com.au)
# save in folders. Use as raw data in a coming fashion-hack-day too 
#
# Input: A json file created after crawling
# 
###########

import json
import urllib
import requests

filename = './iconic.json'

with open(filename,'r') as f:
	datastore = json.load(f)
length = len(datastore)
x = 0
for item in datastore:
	x = x+1
	imgfile = urllib.request.urlopen(item['imageurl'])
	if(x%100==0):
		print('Downloading: ('+str(x)+'/'+str(length)+')')
	with open('./image/'+str(x)+'.jpg','wb') as image:
		image.write(imgfile.read())
		image.close()
	with open('./text/'+str(x)+'.txt','w') as text:
		text.write(item['text'])
		text.close()
