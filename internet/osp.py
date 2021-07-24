import urllib2
s="hello word"
print s[:-1]

LOGIN="username"
PASS="password"
URL="http://localhost"

def handler_version(url):
    from urlparse import urlparse
    handler = urllib2.HTTPBasicAuthHandler()
    handler.add_password('Archives', urlparse(url)[1], LOGIN, PASS)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = urllib2.Request(url)
    bs64_str = encodestring("%s:%s" % (LOGIN, PASS))[:-1]
    req.add_header("Authorization", "Basic %s" % bs64_str)
    return req

for funcType in ('handler', 'request'):
    print "**** Using %s: " % funcType.upper()
    url = eval('%s_version' % funcType)(URL)
    fz = urllib2.urlopen(url)
    print fz.readline()
    fz.close()
    
