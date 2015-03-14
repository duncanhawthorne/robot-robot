import logging, sys, urllib2, os

import sys
# sys.path.insert(0, 'libs') #"Old" way, not working for me.
sys.path.append(os.path.join(os.path.dirname(__file__), "libs")) # This works!

def import_gdoc(docid):
 doc_url = "https://docs.google.com/document/d/"+docid+"/export?format=txt"
 try:
   import urllib2
   doc = urllib2.urlopen(doc_url, timeout =60).read()
   doc = doc.replace("\xef\xbb\xbf","").replace("\xe2\x80\x9c",'"')
   doc = doc.replace("\xe2\x80\x9d",'"').replace("\r","")
   doc = doc.replace("\xe2\x80\x98","'").replace("\xe2\x80\x99","'")
   return doc
 except:
   return 'print("Failed to download source code '+docid+'")'

if False:
	print("alive")
else:
	if os.environ["SERVER_NAME"] == 'robot-robot.appspot.com':
		doc_id = "1UMWDKs5ud2ywzI83oP9HWagA7jiUcZgBtkVrH0Ypktc"
	else:
		doc_id = "1UMWDKs5ud2ywzI83oP9HWagA7jiUcZgBtkVrH0Ypktc"
	
	doc = import_gdoc(doc_id)
	try:	  
	  exec(doc)
	except:
	  logging.debug(str(sys.exc_info()))
	  print(str(sys.exc_info()).replace("<","&lt;").replace(">","&rt;"))
	  print("Crash on running code in doc "+doc_id)
