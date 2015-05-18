#############################################################################
## Read in a tab-delimited file                                            ##
## Edited: December 15, 2014                                               ## 
##                                                                         ##
#############################################################################

###############################################################################
## Readin a tab-delimited file and return a list of values separated by tabs ##
##                                                                           ##
###############################################################################

def readInFile(fileName):
    totalList = []
    dataList = []
    for line in open(fileName):
        for item in line.split("\t"):
            if "\n" in item:                #\n
                index = item.index("\n")    #\n
                dataList.append(item[:index])
                totalList.append(dataList)
                dataList = []
                #dataList.append(item[index:]) # delete this if \n
            else:
                dataList.append(item)
    totalList.append(dataList)
            
    return totalList