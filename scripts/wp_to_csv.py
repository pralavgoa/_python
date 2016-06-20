import csv
import re
import os

def parseFile(filename):
	file = open("input/"+filename,'r').read()	
	outputFile = "output/" + filename + ".csv"
	writeToCsvFile(outputFile,[('slide_title','slide_num','image_name','image_alt','image_attribution','slide_content')])
	writeToCsvFile(outputFile,getHeader(file))
	writeToCsvFile(outputFile,getRemainingSlides(file))

def getHeader(file):
	return re.findall(r"\[tps_header\].+?class=\"(.+?)\".+?href=\"(.+?)\".+?src=\"(.+?)\".+?alt=\"(.+?)\".+?<p.+?>(.+?)</p>.+?</div>\n?(.+?)\n?\[\/tps_header\]",file,re.M|re.S)

def getRemainingSlides(file):
	return re.findall(r"(?:\[tps_header\].+?\[\/tps_header\]\n?)*?\[tps_title\](.+?)\[\/tps_title\].?<a href=\"(.+?)\".+?src=\"(.+?)\".+?alt=\"(.+?)\".+?<p.+?>(.+?)<\/p>\n?(.+?)\n?<!--nextpage-->",file,re.M|re.S)
	
def writeToCsvFile(outputFile,data):
  	with open(outputFile,"ab") as f:
    		writer = csv.writer(f)
    		writer.writerows(data)

def analyseInputFiles():
	for fn in os.listdir('./input'):
		if os.path.isfile('./input/'+fn):
        		print 'Running on file: '+fn
        		parseFile(fn)

analyseInputFiles()
