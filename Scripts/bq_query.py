from login import loginIplant 
from bqapi.comm import BQSession, BQCommError

def main() :
	sess = loginIplant()
	data_service = "http://bovary.iplantcollaborative.org/data_service/" 
	query_type = raw_input("query type [dataset, image]: ")

	query_result = bq_query(sess, data_service, query_type)
	val_to_return = raw_input("return as a list of [uri, filename, time]: ")
	returned_val = bq_query_result(query_result, val_to_return)
	print returned_val

def bq_query(session, data_service, query_type) :
	if (query_type == "dataset") :
		keyword = raw_input("datset name: ") 
		ds = session.query('dataset',name=keyword)
		return ds

	else :
		tag_name = raw_input("tag name [i.e. filename]: ")
		tag_val = raw_input("tag value [add * at the end for wild type]: ")
		images = session.query ('image', tag_query=tag_name+":"+tag_val)
		return images

def bq_query_result(query, value) :
	return_list = []
	for item in query:
		if(value == "uri") :
			return_list.append(item.uri)
		elif(value == "filename") :
			return_list.append(item.name)
		elif(value == "time") :
			return_list.append(item.ts)
	return return_list
main()
