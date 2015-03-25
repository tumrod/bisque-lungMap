from readInFile_r import readInFile_r
from readInFile import readInFile

###############################################################################
## getFileName() parameters                                                  ##
##               - theList, can be from getList() or list of filenames,      ##
##               which has matched names with filenames on bisque images     ##
##               - index, the index of the names or filenames                ##
##               - word, additional string,                                  ##
##               which can be the file extension, for example, ".jpg"        ##
###############################################################################
def getFileName(theList,index, word):
    names = []
    for i in range(len(theList)):
        names.append(theList[i][index]+word)
    return names

###############################################################################
## Annotate images from the annotation/tags list                             ##
##                                                                           ##
###############################################################################
'''
import getpass
import logging

from bqapi import BQSession
'''
import datetime
from login import loginIplant 
from bqapi.comm import BQSession, BQCommError


# logging in
sess = loginIplant()

read_in_names = readInFile("/Users/tumrod/Documents/TACC/bisque-lungMap/tests/5tests_gp.txt")
read_in_annotations = readInFile_r("/Users/tumrod/Documents/TACC/bisque-lungMap/input/completeAnnotation.txt")
name_list = getFileName(read_in_names, 0,"")
annotation_list = getFileName(read_in_annotations, 0,"")

timestamp = datetime.datetime.now().strftime("%I:%M-%m-%d-%Y")

for i in range(len(annotation_list)):
    for j in range(len(name_list)):
        if(name_list[j] == annotation_list[i]):
            #images = sess.query ('image', tag_query="filename:"+name_list[j])
            images = sess.query ('image', tag_query="filename:"+name_list[j])
            for image in images:
                # print image
                sess.clearTags(image.addTag(image.name))
                tag = image.addTag("filename", image.name)
                sess.save(tag)
                tag = image.addTag("upload_datetime", image.ts)
                sess.save(tag)
                tag = image.addTag("lastUpdate", timestamp)
                sess.save(tag)
                for k in range(len(read_in_annotations[0])):
                    tag = image.addTag(read_in_annotations[0][k], read_in_annotations[i][k])
                    sess.save(tag)
                    #tag = read_in_annotations[0][k] +" =\t"+ read_in_annotations[i][k]
                    #print tag


#nameList = getFileName(theList, 0,"")

'''
HOST="http://bovary.iplantcollaborative.org/"

# get username
USER= raw_input("user: ")
#USER= "<USERNAME>" 	#for static username

# get password
PASS= getpass.getpass()

timestamp = datetime.datetime.now().strftime("%I:%M-%m-%d-%Y")

#  authenticate a CAS session
logging.basicConfig (level = logging.DEBUG)

# unccomment to keep the log file
# logging.basicConfig(filename = timestamp + '.log', filemode = 'w', level = logging.DEBUG)
sess  = BQSession()
sess.init_cas(USER, PASS, bisque_root = HOST, create_mex = False)

# get the list of file names
theList = getList()
#print theList[0]

nameList = getFileName(theList, 0,"")
# ex. filename: Asrgl1_Lung.png 
#     official gene symbol: Arsgl1 in index = 2

# go through each image and add annotations for that image from annotation spreadsheet

#print sess.fetchxml('/data/dataset')
for i in range(len(nameList)):
    #for k in range(len(theList[0])):
            #tag = image.addTag(theList[0][k], theList[i][k])
            #tag = theList[0][k] +" =\t"+ theList[i][k]
            #print tag
    
    images = sess.query ('image', tag_query="filename:"+nameList[i])
    
    for image in images:
        # print image
        sess.clearTags(image.addTag(image.name))
        tag = image.addTag("filename", image.name)
        sess.save(tag)
        tag = image.addTag("upload_datetime", image.ts)
        sess.save(tag)
        tag = image.addTag("lastUpdate", timestamp)
        sess.save(tag)

        for k in range(1, len(theList[0])):
            tag = image.addTag(theList[0][k], theList[i][k])
            sess.save(tag)
    
'''
