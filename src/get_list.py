from readInFile_r import readInFile_r
import sys

##############################################################################
## Generating a list of annotations from file                               ##
## The file must be tab-delimited txt file                                  ##
##                                                                          ##
##############################################################################
def getList():
    totalList = []
    annotationList = []
    
    # open file
    #fileName = raw_input("Enter annotation file location: ")
    fileName = sys.argv[1]
    totalList = readInFile_r(fileName)

    return totalList

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