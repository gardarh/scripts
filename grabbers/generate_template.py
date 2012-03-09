#!/usr/bin/python
import urllib2, codecs
from lxml import etree

# opens a page, replaces parts of it with simple tags
# and finally converts the whole thing to the desired encoding
DEV = False
url = "http://www.bondi.is/pages/23/newsid/81"
filename = "/Users/gardarh/bondi/contents.html"
from_encoding = 'UTF-8'
to_encoding = 'ISO-8859-1'
new_base = "http://www.bondi.is/"
outfile = "/Users/gardarh/bondi/template.html"

def main():

	parser = etree.HTMLParser(recover=True)

	if not DEV:
		code = urllib2.urlopen(url).read()
		f = open(filename,'w')
		f.write(code)
		f.close()

	f = codecs.open(filename,encoding=from_encoding)
	code = f.read()
	f.close()

	tree = etree.fromstring(code,parser)
	tree.find('.//title').text = '{{ TITLE }}'
	heading = tree.find('.//div[@class="title"]').find('./h1')
	heading.text = '{{ HEADING }}'
	content = tree.find('.//div[@class="content"]')
	clearfix = content.find('./div[@class="clearfix"]')
	content.remove(clearfix)
	content.text = "{{ CONTENT }}"

	outstring = etree.tostring(tree, method='html', pretty_print=True, encoding=from_encoding)
	outstring = outstring.replace('"/','"%s' % (new_base,)).replace(from_encoding,to_encoding)
	outhandle = open(outfile,'w')
	# Output 8859-1 to avoid problems with converting php codebase to utf-8
	outhandle.write(outstring.decode(from_encoding,errors='ignore').encode(to_encoding,errors='ignore'))
	outhandle.close()

if __name__ == "__main__":
	main()
