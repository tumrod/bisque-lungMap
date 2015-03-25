from readInFile_r import readInFile_r
from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.util import save_blob
from xml.etree import ElementTree as etree

def getFileName(theList,index, word):
    names = []
    for i in range(len(theList)):
        names.append(theList[i][index]+word)
    return names


# logging in
sess = loginIplant()

theList = readInFile_r("/Users/tumrod/Documents/TACC/bisque-lungMap/analysis/44_FinalCandidate_Normalized.txt")
geneList = getFileName(theList, 1,"")
uri_list = []
genes_in_gp = []
is_in_gp = False
not_in_gp = []
img_name_list =[]
info_list = []
info_list.append(theList[0])
info_list.append(theList[1])
for i in range(2,len(geneList)):
    images = sess.query ('image', tag_query=geneList[i])
    #print geneList[i] + "\n"
    for image in images:
        img_name_list.append(image.name)
        is_in_gp = True
        genes_in_gp.append(geneList[i])
        uri_list.append(image.uri)
        
        info_list.append(theList[i])
    if(is_in_gp == False) :
        not_in_gp.append(geneList[i])
    is_in_gp = False

print info_list
print img_name_list
print genes_in_gp
f = open('/Users/tumrod/Documents/TACC/bisque-lungMap/analysis/13_Final_Normalized_heatmap.txt', 'w')
for k in range(len(info_list)):
    for j in range(len(info_list[k])):
        s = info_list[k][j] + "\t"
        f.write(s)
    f.write("\n")
'''

data_service = "http://bovary.iplantcollaborative.org/data_service/" 
datasetname = '44_HCR_Probe_HeatMap'
dataset = etree.Element('dataset',name = datasetname)
for img in uri_list:
    v = etree.SubElement (dataset, 'value', type='object') 
    v.text = img
sess.postxml(data_service +"dataset/",dataset)
'''

'''
print uri_list
print genes_in_gp
print not_in_gp
'''


