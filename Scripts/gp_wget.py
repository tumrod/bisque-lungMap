import subprocess

#################################################################################################

def readInFile():
    totalList = []
    dataList = []
    
    for line in open('/Users/tumrod/Documents/TACC/GenePaint/genepaintTest.txt'):
        for item in line.split("\t"):
            if "\n" in item:
                index = item.index("\n")
                dataList.append(item[:index])
                totalList.append(dataList)
                dataList = []
            else:
                dataList.append(item)
    totalList.append(dataList)
            
    return totalList

# http://gp3.mpg.de/GP-IMG/JPG/EB/EB00001786/EB00001786_00020B.jpg
# cd /corral-repl/tacc/bio/STIR-data/lungmap

def getUrlNameList(imgList):
    fullUrlList = []
    rootURL = "http://gp3.mpg.de/GP-IMG/JPG/"

    for i in range(1,len(imgList)):
        baseName = imgList[i][3]
        setName = baseName[0:10]
        projectID = imgList[i][4]
        urlName = rootURL + projectID + "/" + setName + "/" + baseName + ".jpg"
        fullUrlList.append(urlName)
    return fullUrlList


imageList = readInFile()
fullUrlList = getUrlNameList(imageList)

# run the wget command for each file
for url in fullUrlList:
    command = "wget " + url
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    index = 0;

    # print individual image progress
    for line in p.stdout.readlines():
        if (index == 0):
            print line,
        index = index + 1

        # comment out the above if statement and comment in only the following line
        # to see individual image progress by percentage
        # print line,

    # wait until finished
    retval = p.wait()