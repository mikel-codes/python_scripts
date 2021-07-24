from os.path import splitext as ospath_splitext, dirname as ospath_dirname, exists as ospath_exists, isdir as ospath_isdir
from os import unlink as os_unlink, mkdir, sep as os_sep
from string import replace as str_repl, find as str_find, lower as str_lowcase
from urlparse import urlparse, urljoin
from urllib import urlretrieve
from htmllib import HTMLParser
from cStringIO import StringIO
from sys import argv
from formatter import AbstractFormatter, DumbWriter

class Retreiver(object):
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)
        pass

    def filename(self, url, deffile="index.htm"):

        parsedUrl = urlparse(url, "http:", 0)
        pathForUrl = parsedUrl[1] + parsedUrl[2]
        extension = ospath_splitext(pathForUrl)
        if extension[1] == "":
            if pathForUrl[-1] == '/':
        
                pathForUrl += deffile
            else:
                pathForUrl += '/' + deffile
                
                pass
            pass

        localDir = ospath_dirname(pathForUrl)
        if os_sep != "/":
            localDir = str_repl(localDir, "/", os_sep)

        if not ospath_isdir(localDir):
            if ospath_exists(localDir): os_unlink(localDir)
            mkdir(localDir)
            pass

        return pathForUrl

    def download(self):
        try:
            downloadPage = urlretrieve(self.url, self.file)
        except (IOError, Exception) as x:
            downloadPage = "*** Error : Invalid url or download Error=> %s" % x.message
            pass
        return downloadPage

    def parseAndGetLinks(self):
        try:
            self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO)))
            self.parser.feed(open(self.file).read())
        except Exception as z:
            print z.message
            pass
        finally:
            self.parser.close()
            pass

        return self.parser.anchorlist
    




class WebCrawler(object):
    count = 0
    def __init__(self, url):
        self.urlQueues = [url]
        self.visitedURL = []
        self.domain = urlparse(url)[1]
        pass

    def getPage(self, url):
        obj = Retreiver(url)
        sitePage = obj.download()
        if sitePage[0] == "*":
            print "internet error > no page download >> no parsed url"
            return
        WebCrawler.count += 1
        print "webcrawlers Auto-generated info"
        print "\n(%s)" % str(WebCrawler.count)
        print "URL -> ", url
        print "FILE ->", sitePage[0]
        self.visitedURL.append(url)

        # hunt down links
        links = obj.parseAndGetLinks()
        for eachLink in links:
            if eachLink[:4] != "http" and str_find("://", eachLink) == -1:
                eachLink = urljoin(url, eachLink)
                pass
            print "LINK ->", eachLink
            
            if str_find(str_lowcase(eachLink), "mailto:") == 1:
                print "discarded 'mailto' link"
                print "moving on"
                continue
            
            if eachLink not in self.visitedURL:
               if str_find(eachLink, self.domain) == -1:
                   print ". discarded link not found in this domain %s" %  self.domain
                   
               else:
                   if eachLink not in self.urlQueues:
                       print "addint new url to url Queues database"
                       self.urlQueues.append(eachLink)
                   else:
                       print "Existing url in queue database"
                       pass
                   pass
            else:
               print "... Already processed /visited url"
               pass
            pass
        pass
    
    def go(self):
       while self.urlQueues:
           url = self.urlQueues.pop()
           self.getPage(url)
           pass
       pass
   

def main():
    if len(argv) > 1:
        url = argv[0]
    else:
        try:
            url = raw_input("Enter starting url -> ")
        except Exception as x:
            url = ""
            pass
        pass
    if not url:
        return

    c = WebCrawler(url)
    c.go()
    pass


if __name__ == '__main__':
    main()










        
            

