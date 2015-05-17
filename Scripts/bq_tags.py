from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.xmldict import xml2d
from bq_query import bq_query
import os

def get_tags() :
	sess = loginIplant()
	data_service = "http://bovary.iplantcollaborative.org/data_service/" 
	query_type = "image"
	query_result = bq_query(sess, data_service, query_type)

	key_list = []
	#new_dict = {}
	dict_list = []
	new_dict = []
	total_list = []

	for i in query_result :
		image_uri = i.uri
		tag = sess.fetchxml(image_uri + '/tag')

		d = xml2d(tag)
		
		for key, value in d.items() :
			v = value
			tag_list = v['tag']

			for t in tag_list :
				if (t['name'] not in key_list) :
					key_list.append(t['name'])
	

	for i in query_result :
		image_uri = i.uri
		tag = sess.fetchxml(image_uri + '/tag')
		d = xml2d(tag)

		for key, value in d.items() :
			v = value
			tag_list = v['tag']
			
			for k in range(len(key_list)) :
				new_dict.append(key_list[k])
				new_dict.append('')
				for a in range(len(tag_list)) :
					t = tag_list[a]

					if(t['name'] == key_list[k]):
						if('value' in t.keys()):
							new_dict[1] = t['value']
						else:
							new_dict[1] = ''
				dict_list.append(new_dict)
				new_dict = []

		total_list.append(dict_list)
		dict_list = []
	return total_list


def tag2spreadsheet(total_list) :
	if ((len(total_list)) < 1) :
		print "Error: Not found any images"
	else :
		cwd = os.getcwd()
		parent_dir = cwd[:len(cwd)-7]
		output_dir = parent_dir + "output/"
		f = open(output_dir+'tags_output.txt', 'w')

		# output key
		for t in range(len(total_list[0])) :
			key = total_list[0][t][0]
			f.write(key + "\t")
		f.write("\n")

		# output values
		for image in total_list :
			for tag in image :
				f.write(tag[1] + "\t")
			f.write("\n")


	'''
	for k,v in dict_list[0].items():
		f.write(str(k) + "\t")
	f.write("\n")
	for count in range(len(dict_list)):

		d = dict_list[count]
		for k, v in d.items():
			f.write(str(v) + "\t")
		f.write("\n")
	'''	

tag_list = get_tags()
tag2spreadsheet(tag_list)