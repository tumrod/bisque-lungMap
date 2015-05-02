from login import loginIplant 
from bqapi.comm import BQSession, BQCommError

def main() :
	sess = loginIplant()
	query_type = 'ds'
	bq_query(sess, query_type,'39_embryos_heatmap')

def bq_query(session, query_type, keyword) :
	data_service = "http://bovary.iplantcollaborative.org/data_service/" 
	ds = session.query('dataset',name="Test_dataset")
	#ds = session.fetchxml('/data_service/dataset', name=keyword)
	for d in ds:
		print d.uri

main()
