from readInFile import readInFile
from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.util import save_blob
from xml.etree import ElementTree as etree



#upload
'''
FG00000055_00008B.jpg
ST00000087_00017B.jpg
EB00000186_00008B.jpg
HD00000008_00008B.jpg
WB00000088_00005B.jpg
EB00000609_00011B.jpg

'''


fileName = raw_input("Annotation file: ")
#fileName = '/Users/tumrod/Documents/TACC/GenePaint/output/completeAnnotation.txt'
annotationList = readInFile(fileName)

# logging in
sess = loginIplant()

# image path
root_path = raw_input("path to image directory: ")
#root_path = '/Users/tumrod/Documents/TACC/GenePaint/images/'

# image file name list
LOCAL_FILE_PATH = raw_input("filenames file <name> : ")
#LOCAL_FILE_PATH = readInFile('/Users/tumrod/Documents/TACC/GenePaint/output/gptest.txt')

# navigate through the list of file name
for image in range(len(LOCAL_FILE_PATH)):
	# create local path of the images
	iname = LOCAL_FILE_PATH[image][0]
	path = root_path + iname
	
    # navigate through the annotation list
	for i in range(len(annotationList)) :
		if(iname == annotationList[i][0][1:]):
            
            # create the image object
			resource = etree.Element ('image', name= iname)
            
            
			for j in range(len(annotationList[i])) :
				#print "name: " + annotationList[0][j] + "\t value: " + annotationList[i][j]
                
                # create the tag as sub element
				etree.SubElement (resource, 'tag', name=annotationList[0][j], value=annotationList[i][j])
            
            # save/ post the xml back
			r = save_blob(sess, path, resource=resource)
            
			if r is None:
				print 'Error uploading'
				#r is a created metadata document in etree form
			uri = r.get('uri')
