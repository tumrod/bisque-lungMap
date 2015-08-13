'''
Resources from http://biodev.ece.ucsb.edu/projects/bisquik/wiki/Developer/ImportService
'''

from bqapi.comm import BQSession, BQCommError
from bqapi.util import save_blob
from login import loginIplant
import sys

# logging in
session = loginIplant()
#session = BQSession().init_local(MY_USER, MY_PASSWD,  bisque_root=BISQUE_ROOT_URL, create_mex=False)

LOCAL_FILE_PATH = sys.argv[1]
print LOCAL_FILE_PATH

r = save_blob(session, LOCAL_FILE_PATH)
if r is None:
    print 'Error uploading'
# r is a created metadata document in etree form
uri = r.get('uri')