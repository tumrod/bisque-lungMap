#############################################################################
## Log-in to iplantcollaborative.org/bisque with CAS initialization        ##
## Edited: December 15, 2014                                               ## 
## Credited to Kris Kvilekval and Dmitry Fedorov                           ##
#############################################################################


import getpass
import logging
from bqapi import BQSession


###### LOGGING IN #######
def loginIplant():
	#HOST= raw_input("host: ")
	
	# default: "http://bovary.iplantcollaborative.org/" for iplant bisque
	HOST="http://bovary.iplantcollaborative.org/"

	# get username
	USER= raw_input("user: ")
	#USER= "<USERNAME>" 	#for static username

	# get password
	PASS= getpass.getpass()

	#  authenticate a CAS session
	logging.basicConfig (level = logging.DEBUG)
	sess  = BQSession()
	sess.init_cas(USER, PASS, bisque_root = HOST, create_mex = False)
	return sess