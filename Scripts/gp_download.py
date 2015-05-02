from readInFile import readInFile
from gp_wget import run_wget

name_list = readInFile("/Users/tumrod/Documents/TACC/Analysis/images/4_img_names.txt")
#print name_list
#name_list = [['HD00000072_00009B']]

root = "http://gp3.mpg.de/GP-IMG/JPG/"
url_list = []

for i in range(len(name_list)) :
    set_name = name_list[i][0][:2]
    set_num = name_list[i][0][:10]
    file_name = name_list[i][0] + ".jpg"
    file_path = root+set_name + "/" + set_num + "/" + file_name
    url_list.append(file_path)

#print url_list

run_wget(url_list)