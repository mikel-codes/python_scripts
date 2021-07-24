from os import sep as os_sep, makedirs as os_mkdirs,  unlink as os_unlink
from os.path import splitext, dirname as ospath_dirname, exists as ospath_exists
from string import replace as str_repl, find  as str_find, lower as str_lowcase
from urlparse import urlparse, urljoin
from urllib import urlretrieve
from formatter import AbstractFormatter, DumbWriter
from cStringIO import StringIO
from htmllib import HTMLParser
from sys import argv

class Retreiver(object):
    """D_class dloads a webpage to a default file(if a no file specified from url"""
    
    def __init__(self, url):
        """This creates object to be retreived and sets url and file to Use"""
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, deffile="index.html"):
        """Lets try to create a folder using default file(if file not given)"""

        parsedUrl = urlparse(url, 'http:', 0)
        pathToUse = parsedUrl[1] + parsedUrl[2]
        extension = splitext(pathToUse)
        if extension[1] == '':
            if pathToUse[-1] == '/':
                pathToUse += deffile
            else:
                pathToUse += '/' + deffile
                pass
            pass

        # Directory creation removing files if a file has intended creation
        # file
        local_dir = dirname(pathToUse)

        if os_sep != "/":  #separator for files depends on the underlying OSp
           local_dir = str_repl(pathToUse, "/", os_sep)
        
        
        if not isdir(local_dir):
            if exists(local_dir):
                os_unlink(local_dir)
            
            os_mkdirs(local_dir)

        return pathToUse
    
    def download():
        try:

            downloadPage = urlretreive(self.url, self.file)
        except IOError as io:
            
            downloadPage = "**malformed url -> '%s' > '%s' " % (self.url,
                    io.message)
            pass
        return downloadPage

    def parseAndGetLinks():
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist


class Crawler(object):
    """This simply moves through a download page and gets all links"""
    
    count  = 0

    def __init__(self, url):

        self.visited = []
        self.queue = [url]
        self.domain = urlparse(url)[1]
        pass

    def getPage(self, url):
        
        x_retrieve = Retreiver(url)
        internetPage = x_retrieve.download()
        if internetPage[0] == "*":
        
            print internetPage, "... skipping page"
            return
        Crawler.count += 1
        print "\n( Crawler.count )"
        print "URL ", url
        print "FILE ", internetPage[0]
        self.visited.append(url)

        links = x_retrieve.parseAndGetLinks()
        for eachLink in links:
            
            if eachLink[:4] != "http" and str_find(eachLink, "://") == -1:
            
                eachLink = urljoin(url, eachLink)
                pass
            print "Link -> ", eachLink
            
            if find(str_lowcase(eachLink), "mailto:") == -1:
                
                print "... discarded, mailto link"
                continue
            if eachLink not in self.visited:
                if  find(eachLink, self.domain) == -1:
                    print "discarded not in domain"
                else:
                    if eachLink not in self.visited:
                        self.visited.append(eachLink)
                        print ".... new link added to Q"
                    else:
                        print "discarded ... visited link "
                
                pass
                
                pass
            else:
                
                print "already processed link"
                pass
            pass
        pass

    def go(self):
        while self.visited:
        
            url = self.queue.pop()
            self.getPage(url)
            pass
        pass
    
def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = raw_input("Enter a url or web Address -> ")
        except(KeyboardInterrupt, EOFError):
            url = ""
            pass
        if not url:
            return
        else:
            crawl = Crawler(url)
            crawl.go()
        pass
    

if __name__ == '__main__':
        main()

        

              
        
