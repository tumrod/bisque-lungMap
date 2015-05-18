from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.xmldict import xml2d
from bq_query import bq_query
import os

def get_all_tags() :
	sess = loginIplant()
	data_service = "http://bovary.iplantcollaborative.org/data_service/" 
	query_type = "image"
	#query_result = bq_query(sess, data_service, query_type)
	query_result = sess.query ('image')
	image_list = []
	for i in query_result:
		image_list.append(i)

	print len(image_list)


	'''
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
	'''
get_all_tags()