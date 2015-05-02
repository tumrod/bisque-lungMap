from login import loginIplant 
from bqapi.comm import BQSession, BQCommError

def main() :
	sess = loginIplant()
	data_service = "http://bovary.iplantcollaborative.org/data_service/" 
	query_type = raw_input("query type [dataset, image]: ")
	
	bq_query(sess, query_type,'39_embryos_heatmap')

def bq_query(session, data_service, query_type) :
	if (query_type == "dataset") :
		keyword = raw_input("datset name: ") 
		ds = session.query('dataset',name=keyword)
		for d in ds:
			print d.uri

	else :
		tag_name = raw_input("tag name [i.e. filename]: ")
		tag_val = raw_input("tag value [add * at the end for wild type]: ")
		images = sess.query ('image', tag_query=tag_name+":"+tag_val)
		
main()
