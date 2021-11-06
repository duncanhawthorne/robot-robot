# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "libs")) # This works!
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)


import logging, urllib2

orig_print = print
orig_print("") #this is necessary so can print strange characters as first thing to print, e.g. {. html files starting with { must be special in some way, so print something blank to get chrome started

def print(x,end=None):
  if type(x) == str:
    None
    #x = x.replace("<","&lt;").replace(">","&rt;")
  orig_print(x.encode('utf-8').strip())
  if end != "":
    orig_print("<br>")

def import_gdoc(docid):
 doc_url = "https://docs.google.com/document/d/"+docid+"/export?format=txt"
 try:
   doc = urllib2.urlopen(doc_url, timeout =60).read().decode('utf-8')
   doc = doc.replace("“",'"').replace("”",'"')
   doc = doc.replace("‘","'").replace("’","'")
   doc = doc.replace(b"\xef\xbb\xbf".decode("utf-8"),"")
   doc = doc.replace("\r","")
   doc = doc.encode('utf-8')
   return doc
 except:
   return 'print("Failed to download source code '+docid+'")'

key_doc_id = "1UMWDKs5ud2ywzI83oP9HWagA7jiUcZgBtkVrH0Ypktc"

doc = import_gdoc(key_doc_id)
try:	  
  exec(doc)
except:
  logging.debug(str(sys.exc_info()))
  print("base python file exception")
  print(sys.exc_info())
  print("Crash on running code in doc "+key_doc_id)
