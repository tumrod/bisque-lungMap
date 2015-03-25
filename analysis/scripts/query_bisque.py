from readInFile import readInFile
from login import loginIplant 
from bqapi.comm import BQSession, BQCommError

def getFileName(theList,index, word):
    names = []
    for i in range(len(theList)):
        names.append(theList[i][index]+word)
    return names

#upload
'''
'''

# logging in
sess = loginIplant()

theList = readInFile("/Users/tumrod/Documents/TACC/bisque-lungMap/analysis/44_FinalCandidate_HCR_probeListHeatmapV2(1)(1).txt")
print theList
#theList = readInFile("/Users/tumrod/Documents/TACC/bisque-lungMap/input/complete_filenames.txt")
#nameList = getFileName(theList, 0,"")
#geneList = getFileName(theList, 1,"")
#uri_list = []
'''
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

