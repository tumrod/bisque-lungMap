from readInFile_r import readInFile_r
from readInFile import readInFile
from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.util import save_blob
from xml.etree import ElementTree as etree
from get_list import *

def upload_main() :
	# image path
	ROOT_PATH = raw_input("path to image directory: ")

	# image file name list
	LOCAL_FILE_PATH = readInFile_r(raw_input("list of filename to be upload : "))

	# logging in
	sess = loginIplant()

	#print LOCAL_FILE_PATH
	#print annotationList
	usr_annotation = raw_input("upload with annotation [y/n]: ")
	done = 0

	while (done != 1) :
		if (usr_annotation == "y") :
			is_annotation = True
			done = 1
		elif (usr_annotation == "n") :
			is_annotation = False
			done = 1
		else :
			print "Error please enter y/n"
			done = 0

	if (done == 1) :
		upload(sess, ROOT_PATH, LOCAL_FILE_PATH, is_annotation)


def upload(sess, ROOT_PATH, LOCAL_FILE_PATH, is_annotation) :

	if (is_annotation) :
		# get the list of annotations
		annotationList = getList()
		print annotationList
		# get FileName list to be query, in this case, assuming the first column of the spreadsheet contain filename
		nameList = getFileName(annotationList, 0,"")  

		print LOCAL_FILE_PATH
		# navigate through the list of file name
		for image in range(len(LOCAL_FILE_PATH)+1):

			# create local path of the images
			iname = LOCAL_FILE_PATH[image][0]
			print iname
			path = ROOT_PATH + "/"+ iname
			print path

		    # navigate through the annotation list
			for i in range(len(annotationList)) :
				print annotationList[i][0]
				print annotationList[i]

				if(iname == annotationList[i][0]):
		            
		            # create the image object
					#resource = etree.Element ('image', name=iname)
		        	
					for j in range(len(annotationList[i])) :
						print "name: " + annotationList[0][j] + "\t value: " + annotationList[i][j]
		                # create the tag as sub element
						#etree.SubElement (resource, 'tag', name=annotationList[0][j], value=annotationList[i][j])
		            
					
					

	else :
		for image in range(len(LOCAL_FILE_PATH)):

			# create local path of the images
			iname = LOCAL_FILE_PATH[image][0]
			#print iname
			path = ROOT_PATH + "/"+ iname
			#print path

			# create the image object
			resource = etree.Element ('image', name= iname)
            
            # save/ post the xml back
			r = save_blob(sess, path, resource=resource)
            
			if r is None:
				print 'Error uploading'
				#r is a created metadata document in etree form
			uri = r.get('uri')
upload_main()
