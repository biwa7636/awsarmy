import urllib
import urllib2
import time
import zlib
import socket
import cookielib
import json

# Global Environment Variable
cookieJar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
opener.addheaders = [('Accept', 'application/json')]
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


def myfunction2(url):
    print url
    content = opener.open(url).read()
    data = {'content': content}
    return data


#TEST
if 1:
    inputList = open('myinput.txt', 'r').readlines()
    outputFile = file('output_test.txt', 'w')
    for element in inputList[:10]:
        print element
        output = myfunction2(element)
        print >>outputFile, output
    outputFile.close()
     
