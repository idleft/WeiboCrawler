import urllib2, urllib

f = urllib2.urlopen(
		url = 'http://www.baidu.com')
print f.read()