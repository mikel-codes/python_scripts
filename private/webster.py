#!/usr/bin/env python
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re

def getLinks(url):
    req = Request(url)
    try:
        page = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print ("Failed to reach server ")
            print ("Reason :", e.reason)
        elif hasattr(e, 'code'):
            print ("Server could not fufill the request")
            print ("Error code : ", e.code)
    else:
        soup = BeautifulSoup(page, "html.parser")
        links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    return links

if __name__ == '__main__':
    anchors = getLinks("http://moregrace.tv/")
    countLinks = len(anchors)
    for anchor in anchors:
        print anchor

    print countLinks
    #for anchor in anchors:
     #   res = urllib.urlrequest.urlopen(anchor)
      #  if res.getcode() == "404":
       #     print "could not retreive url page"

        #countMe = getLinks()


