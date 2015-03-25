def readInFile_r(fileName):
    totalList = []
    dataList = []
    for line in open(fileName):
        for item in line.split("\t"):
            if "\r" in item:                #\n
                index = item.index("\r")    #\n
                dataList.append(item[:index])
                totalList.append(dataList)
                dataList = []
                dataList.append(item[index+1:]) # delete this if \n
            else:
                dataList.append(item)
    totalList.append(dataList)
            
    return totalList