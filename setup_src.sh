#!/bin/bash
mv extra_src/beautifulsoup4-4.3.2-py2.7.egg bqapi/lib/python2.7/site-packages/
mv extra_src/easy-install.pth bqapi/lib/python2.7/site-packages/
mv extra_src/comm.py bqapi/lib/python2.7/site-packages/bqapi

for i in ./extra_src/*/;
do
	mv "$i" bqapi/lib/python2.7/site-packages/
done
