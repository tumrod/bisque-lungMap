#############################################################################
## query images by dataset or tags on iplant/bisque                        ##
## Edited 2: May 2, 2015                                            	   ##                                 
## query and return a list of either uri, filename, etc.                   ##
#############################################################################

###############################################################################
## Query for images from tags(key and value) or from dataset name            ##
## Return a list of uri, filename, etc. as requested from console            ##
###############################################################################


from login import loginIplant 
from bqapi.comm import BQSession, BQCommError
from bqapi.xmldict import xml2d

def query_main() :
	sess = loginIplant()
	data_service = "http://bovary.iplantcollaborative.org/data_service/" 

	# user specifies the type of query
	query_type = raw_input("query type [dataset, image]: ")
	query_result = bq_query(sess, data_service, query_type)

	# user specifies the return value
	val_to_return = raw_input("return as a list of [uri, filename, time]: ")
	returned_val = bq_query_result(query_result, val_to_return)

	print returned_val
	return returned_val

# query by passing in the parameter specified by the user
def bq_query(session, data_service, query_type) :
	if (query_type == "dataset") :
		keyword = raw_input("datset name: ") 
		ds = session.query('dataset',name=keyword)
		return ds

	else :
		tag_name = raw_input("query key [i.e. filename]: ")
		tag_val = raw_input("query value [add * at the end for wild type]: ")
		images = session.query ('image', tag_query=tag_name+":"+tag_val)
		return images

# return a list of query result to be returned
def bq_query_result(query, value) :

	return_list = []
	for item in query:
		print item
		if(value == "uri") :
			return_list.append(item.uri)
		elif(value == "filename") :
			return_list.append(item.name)
		elif(value == "time") :
			return_list.append(item.ts)
	return return_list
