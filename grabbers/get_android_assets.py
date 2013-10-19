import os, urllib

DSTDIR = "/Users/gardarh/checkbox_android_resources/"

def main():
	url_template = "https://github.com/android/platform_frameworks_base/raw/master/core/res/res/drawable-%s/btn_check_%s%s_holo_dark.png"
	dpis = ['mdpi','hdpi','xhdpi']
	onoff = ['on','off']
	states = ['', 'pressed','focused','disabled','disabled_focused']

	for dpi in dpis:
		for onoff_state in onoff:
			for state in states:
				if state:
					# All other states then None state
					state = '_%s' % (state,)
				url = url_template % (dpi, onoff_state, state)
				filename = url.rsplit('/',1)[-1]
				dirname = '%s%s' % (DSTDIR, 'drawable-%s/' % (dpi,))
				print dirname
				if not os.path.exists(dirname):
					os.makedirs(dirname)
				abs_filename = '%s%s' %  (dirname, filename)
				dl_result = urllib.urlretrieve (url, abs_filename)
				print "Downloading %s" % (url,)
				print dl_result[1]

if __name__ == "__main__":
	main()
