###########
# Created by Jizhizi Li @ 07/11/2017
# A simple download function to download images and texts
# after crawling from Iconic website (https://www.theiconic.com.au)
# save in folders. Use as raw data in a coming fashion-hack-day too 
#
# Input: A path of json file and number of item
# 
###########

import json
import urllib
import requests
import sys


itemnumber = sys.argv[2]
filename = str(sys.argv[1])

with open(filename,'r') as f:
	datastore = json.load(f)
length = len(datastore)
x = 0
for item in datastore:
	x = x+1
	try:
		imgfile = urllib.request.urlopen(item['imageurl'])
		with open('./data/image/'+str(itemnumber)+'/'+str(x)+'.jpg','wb') as image:
			image.write(imgfile.read())
			image.close()
	except:
		with open('./data/text/'+str(itemnumber)+'.txt','w') as text:
			for textItem in item['text']:
				text.write("%s\n" % textItem)
			text.close()
