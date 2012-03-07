import urllib2, codecs
from lxml import etree
DEV = True

# Replaces certain spots in a page with placeholders

def main():
	url = "http://www.bondi.is/pages/23/newsid/81"
	filename = "contents.html"
	encoding = 'UTF-8'
	new_base = "http://www.bondi.is/"
	outfile = "template.html"

	parser = etree.HTMLParser(recover=True)

	if not DEV:
		code = urllib2.urlopen(url).read()
		f = open(filename,'w')
		f.write(code)
		f.close()

	f = codecs.open(filename,encoding=encoding)
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

	outstring = etree.tostring(tree, method='html', pretty_print=True, encoding=encoding)
	outstring = outstring.replace('"/','"%s' % (new_base,))
	outhandle = open(outfile,'w')
	outhandle.write(outstring)
	outhandle.close()

if __name__ == "__main__":
	main()
