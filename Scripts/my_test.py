from bqapi import BQSession

#####################################
####           EDITED           #####
####           PUT xml          #####
#####################################
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

BQSession.putxml = putxml
###############################################################################################
###             EDITED                                                                      ###
###             Clear all of the existed clearTags                                          ### 
###############################################################################################

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
BQSession.clearTags = clearTags