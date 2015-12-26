# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Version python : 2.7.9
# Description : ajoute une colonne contenant le nom de domaine extrait des URLS
# Utilisation :  python extraire.py url.csv

import string
import csv
import re
import urllib2
import traceback
import httplib
from urlparse import urlparse
import os
import sys

class main:
	cr = csv.reader(open(sys.argv[1],"rb"))
	i=0
	divers=0
	liste=[]
	liste_domain=[]
	file = open('extract.'+sys.argv[1], "w")

	print "\nTraitement : \n"
	for row in cr:	
		if row[1]:
			i=i+1
			#print row[1]
			parsed_uri = urlparse(row[1])
			domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
			#print domain
			
			elem = row[0]+","+row[1]+","+domain
			#print elem
			liste.append(elem)
			liste_domain.append(domain)
	total=len(liste)
	print "Total URLs : ",total,'\n'
	
	liste_sansdoublons=list(set(liste_domain))
	total_sansdoublons = len(liste_sansdoublons)
	#print "Total URLs uniques",len(liste_sansdoublons)
	
	for elem in liste_sansdoublons:
		nb_domain=liste_domain.count(elem)
		if nb_domain>=total/100: 
			print elem,' : ',"%.1f" %(float(nb_domain)/float(total)*100),'%'
		else:
			divers = nb_domain+divers
	print 'divers <1%',' : ',"%.1f" %(float(divers)/float(total)*100),'%'
	file.write("\n".join(liste))
	file.close()
