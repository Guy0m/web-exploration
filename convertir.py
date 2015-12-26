# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Version python : 2.7.9
# Description : convertir des URLs raccourcis en URLs completes
# Utilisation :  python convertir.py url.txt

import string
import csv
import re
import urllib2
import traceback
import httplib
import os
import sys


class main:
	reussi=0
	file = open('full.'+sys.argv[1], "w")
	nb_URLs = str(sum(1 for _ in open(sys.argv[1])))
	print 'nb_URLS dans le fichier',sys.argv[1],' : '+ nb_URLs
	with open(sys.argv[1], 'r') as f:
		for line in f:
			try: 
				rep = urllib2.urlopen(line)
				#print rep.geturl()	
				file.write(rep.geturl()+"\n")
				reussi=reussi+1
				print 'Nb_URLs convertis : ',reussi,'/',nb_URLs
			except urllib2.HTTPError, e:
				print 'erreur '+str(e.code)
			except urllib2.URLError, e:
				print 'erreur '+str(e.reason)
			except httplib.HTTPException, e:
				print 'erreur HTTPException'
			except Exception:
				print 'erreur '+traceback.format_exc()
				
	print 'Nb_URLs convertis final : ',reussi,'/',nb_URLs
	print '\nResultat : '+ file.name
