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
import os
import sys

# logging in
sess = loginIplant()

timestamp = datetime.datetime.now().strftime("%I:%M-%m-%d-%Y")
count=0

cwd = os.getcwd()
parent_dir = cwd[:len(cwd)-7]
output_dir = parent_dir + "output/"

# output filename with time specified
timestamp = datetime.datetime.now().strftime("%y%m%d-%I%M")
#f = open(output_dir+timestamp+'_deleted_files.txt', 'w')

key_to_delete = sys.argv[1]
images = sess.query ('image', tag_query="*"+key_to_delete+"*")
for image in images:
    count+=1
    print count, image.name, image.uri,
    result = str(count) + " " + str(image.name) + " " + str(image.uri) + " "
    #f.write(result)
    sess.delete(image)
    print "\tDELETED!"
    #f.write("\tDELETED!\n")
        
    
print "Total images: ", count
#f.write("Total images: " + str(count) + "\n")

