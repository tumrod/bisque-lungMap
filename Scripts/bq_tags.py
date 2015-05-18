#############################################################################
## Fetch tags/annotations from iplant/bisque                               ##
## Edited: May 15, 2015                                            	       ##
## Last Edited: May 17, 2015                                               ##                                 
## Query images, fetch tags and return as a tab-delimited file             ##
#############################################################################

###############################################################################
## Query images, and fetch tags from them						             ##
## Return a spreadsheet consists of annotations as a column, image as a row  ##
###############################################################################

from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.xmldict import xml2d
from bq_query import bq_query
import os
import datetime


def bq_tags_main() :
	sess = loginIplant()
	data_service = "http://bovary.iplantcollaborative.org/data_service/" 
	query_type = "image"

	print "Would you like to do query? [y/n]"
	is_query = raw_input("[y] for query by keyword; [n] for customs: ")

	if ((is_query == 'y') or (is_query == 'Y')):
		query_result = bq_query(sess, data_service, query_type)
		tag_list = query_to_tags(sess, query_result)
		tag2spreadsheet(tag_list)

	elif ((is_query == 'n') or (is_query == 'N')):
		is_all = raw_input("CUSTOMS: [y] for all images, [n] for limit: ")
		if ((is_all == 'y') or (is_all == 'Y')):
			query_result = sess.query ('image')
			tag_list = query_to_tags(sess, query_result)
			tag2spreadsheet(tag_list)

		elif ((is_query == 'n') or (is_query == 'N')):
			query_limit = raw_input("limit: ")
			query_offset = raw_input("offset: ")
			query_result = sess.query('image', limit=query_limit, offset=query_offset)
			tag_list = query_to_tags(sess, query_result)
			tag2spreadsheet(tag_list)
		else:
			print "please enter [y] or [n]"

	else:
		print "please enter [y] or [n]"


	return query_result

def query_to_tags(sess, query_result) :

	key_list = []

	# iterate through the query_result to get all of the keys/ tag's name
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
	

	#######################################################################
	# in a process of DEBUGGING and furnishing the structure/ performance

	dict_list = []
	new_dict = []
	total_list = []

	# second iteration for the tags of each image
	for i in query_result :
		image_uri = i.uri
		tag = sess.fetchxml(image_uri + '/tag')
		d = xml2d(tag)

		for key, value in d.items() :
			v = value
			tag_list = v['tag']
			
			# initialized all of the key:value to key:''
			for k in range(len(key_list)) :
				new_dict.append(key_list[k])
				new_dict.append('')

				# compare and input the actual value of the key
				for a in range(len(tag_list)) :
					t = tag_list[a]

					if(t['name'] == key_list[k]):
						if('value' in t.keys()):
							new_dict[1] = t['value']
						else:
							new_dict[1] = ''

				# append to the list of key:value for each image
				dict_list.append(new_dict)
				new_dict = []

		# append the list of image's tags to total list of all images
		total_list.append(dict_list)
		dict_list = []
	return total_list


# from tag list to a spreadsheet
def tag2spreadsheet(total_list) :
	if ((len(total_list)) < 1) :
		print "Error: Not found any images"
	else :
		# output the file into the output directory, which is bisque-lungMap/output
		# assume current working directory is bisque-lungMap/Scripts
		cwd = os.getcwd()
		parent_dir = cwd[:len(cwd)-7]
		output_dir = parent_dir + "output/"
		
		# output filename with time specified
		timestamp = datetime.datetime.now().strftime("%y-%m-%d-%I%M")
		f = open(output_dir+timestamp+'_tags_output.txt', 'w')

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

bq_tags_main()