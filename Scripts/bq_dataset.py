from readInFile import readInFile
from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.util import save_blob
from xml.etree import ElementTree as etree

def getFileName(theList,index, word):
    names = []
    for i in range(len(theList)):
        names.append(theList[i][index]+word)
    return names

#upload
'''
FG00000055_00008B.jpg
ST00000087_00017B.jpg
EB00000186_00008B.jpg
HD00000008_00008B.jpg
WB00000088_00005B.jpg
EB00000609_00011B.jpg

HD00000061_00005B.jpg
WB00000023_00015B.jpg
'''

# logging in
sess = loginIplant()

#theList = readInFile("/Users/tumrod/Documents/TACC/bisque-lungMap/tests/5tests_gp.txt")
theList = readInFile("/Users/tumrod/Documents/TACC/bisque-lungMap/input/complete_filenames.txt")
nameList = getFileName(theList, 0,"")
uri_list = []

for i in range(len(nameList)):
    images = sess.query ('image', tag_query="filename:"+nameList[i])
    for image in images:
    	print image.uri
    	uri_list.append(image.uri)

data_service = "http://bovary.iplantcollaborative.org/data_service/" 

datasetname = 'full_gene_paint'
dataset = etree.Element('dataset',name = datasetname)
for img in uri_list:
	v = etree.SubElement (dataset, 'value', type='object') 
	v.text = img
sess.postxml(data_service +"dataset/",dataset)


'''
data_service = "http://bovary.iplantcollaborative.org/data_service/" 
ds = sess.query('dataset',name="restored")
for d in ds:
	dataset = d.toetree(d.parent,d.uri)
	print dataset
	for img in uri_list:
		v = etree.SubElement (dataset, 'value', type='object') 
		v.text = img
		print v
	sess.postxml(data_service +"dataset/",dataset)
'''

