#############################################################################
## LungMap Tags Annotation on Bisque                                       ##
## Edited 2: December 15, 2014                                             ##
## Last Edited: January 13, 2015                                           ##
## Multiple images annotations from tab delimited file                     ##
#############################################################################

###############################################################################
## Annotate images from the annotation/tags list                             ##
## Credited to Kris Kvilekval and Dmitry Fedorov                             ##
###############################################################################

import getpass
import logging
import datetime
from bqapi import *
from get_list import *
from login import loginIplant
from types import MethodType

def clearTags(self, bqo, url=None, **kw):
    try:
        original = bqo
        
        # Find an object (or parent with a valild uri)
        url = url or bqo.uri
        if url is None:
            url = bqo.parent.uri
            while url is None and bqo.parent:
                bqo = bqo.parent
                url=  bqo.parent.uri
        if url is None:
            raise BQApiError("Can't determine save url for %s" % original)
        
        xml =  self.factory.to_etree(bqo)
        xml = self.putxml(url, xml, method="PUT", **kw)
        return xml is not None and self.factory.from_etree(xml)
    except BQCommError, ce:
        log.exception('communication issue while saving %s' % ce)
        return None

def putxml(self, url, xml, path=None, method="PUT", **params):
    if not isinstance(xml, basestring):
        xml = self.factory.to_string(xml)
    log.debug('putxml %s content %s ' %(url, xml))

    url = self.c.prepare_url(url, **params)

    try:
        r = None
        if not self.dryrun:
            r = self.c.push(url, content=xml, method=method, path=path, headers={'Content-Type':'text/xml', 'Accept': 'text/xml' })
        if path is not None:
            return r
        return r and self.factory.string2etree(r)
    except etree.ParseError, e:
        log.exception("Problem with put response %s", e)
        return r


def main() :
    # get the list of annotations
    theList = getList()

    # get FileName list to be query, in this case, assuming the first column of the spreadsheet contain filename
    nameList = getFileName(theList, 0,"")  

    # logging in
    sess = loginIplant()

    sess.clearTags = MethodType(clearTags, sess, BQSession)
    sess.putxml = MethodType(putxml, sess, BQSession)

    timestamp = datetime.datetime.now().strftime("%I:%M-%m-%d-%Y")

    # go through each image and add annotations for that image from annotation spreadsheet
    for i in range(len(nameList)):
        
        # query by the filename
        images = sess.query ('image', tag_query="filename:"+nameList[i]+"*")
        
        for image in images:
            
            # clear all of the annotations
            sess.clearTags(image.addTag(image.name))

            # re-input pre-existed annotation
            tag = image.addTag("filename", image.name)
            sess.save(tag)
            tag = image.addTag("upload_datetime", image.ts)
            sess.save(tag)
            tag = image.addTag("lastUpdate", timestamp)
            sess.save(tag)
            
            # create new annotation from the annotation list
            for k in range(1, len(theList[0])):
                tag = theList[0][k] +" =\t"+ theList[i][k]
                #print tag
                tag = image.addTag(theList[0][k], theList[i][k])
                sess.save(tag)

if __name__ == '__main__':
    main()

