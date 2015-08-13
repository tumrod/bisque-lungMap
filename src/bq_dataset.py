#############################################################################
## Create Dataset on iplant/bisque                                         ##
## Edited 2: May 2, 2015                                            	   ##                                        ##
##                                                                         ##
#############################################################################

###############################################################################
## Create a dataset from existed images in Bisque                            ##
##                                                                           ##
###############################################################################

from readInFile import readInFile
from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.util import save_blob
from xml.etree import ElementTree as etree
from get_list import *

def ds_create_main() :
	# logging in
	sess = loginIplant()

	# get the list of annotations
	theList = getList()

	# get FileName list to be query, in this case, assuming the first column of the spreadsheet contain filename
	nameList = getFileName(theList, 0,"")

	uri_list = get_uri_list(sess, nameList)
	dataset_name = raw_input("Dataset name: ")
	create_dataset(sess,"http://bovary.iplantcollaborative.org/", dataset_name, uri_list)

# get a list of uri from query by filename
def get_uri_list(sess, nameList) :
    uri_list = []
        
    for i in range(len(nameList)):
        images = sess.query ('image', tag_query="filename:"+nameList[i])
        for image in images:
            uri_list.append(image.uri)
    return uri_list

# create a dataset
def create_dataset(sess, hostname, datasetname, uri_list) :
	data_service = hostname + "data_service/" 
	dataset = etree.Element('dataset',name = datasetname)

	for img in uri_list:
		v = etree.SubElement (dataset, 'value', type='object') 
		v.text = img
	sess.postxml(data_service +"dataset/", dataset)

if __name__ == '__main__':
    ds_create_main()



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


