#############################################################################
## LungMap Tags Annotation on Bisque                                       ##
## Edited 2: December 15, 2014                                             ##
## Last Edited: January 13, 2015                                           ##
## Multiple images annotations from tab delimited file                     ##
#############################################################################

###############################################################################
## Annotate images from the annotation/tags list                             ##
## Credited to Kris Kvilekval and Dmitry Fedorov                             ##
###############################################################################

import getpass
import logging
import datetime
from bqapi import BQSession
from get_list import *
from login import loginIplant 

# get the list of annotations
theList = getList()

# get FileName list to be query, in this case, assuming the first column of the spreadsheet contain filename
nameList = getFileName(theList, 0,"")  

# logging in
sess = loginIplant()

timestamp = datetime.datetime.now().strftime("%I:%M-%m-%d-%Y")

# go through each image and add annotations for that image from annotation spreadsheet
for i in range(len(nameList)):
    
    # query by the filename
    images = sess.query ('image', tag_query="filename:"+nameList[i]+"*")
    
    for image in images:
        
        # clear all of the annotations
        sess.clearTags(image.addTag(image.name))

        # re-input pre-existed annotation
        tag = image.addTag("filename", image.name)
        sess.save(tag)
        tag = image.addTag("upload_datetime", image.ts)
        sess.save(tag)
        tag = image.addTag("lastUpdate", timestamp)
        sess.save(tag)
        
        # create new annotation from the annotation list
        for k in range(1, len(theList[0])):
            tag = theList[0][k] +" =\t"+ theList[i][k]
            #print tag
            tag = image.addTag(theList[0][k], theList[i][k])
            sess.save(tag)
        
    

