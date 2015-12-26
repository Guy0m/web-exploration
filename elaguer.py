# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Version python : 2.7.9
# Description : Supprimer les doublons et liens trop courts t.co
# Utilisation :  elaguer.py url.txt

import string
import csv
import sys
import os

class main:
	file = list(open(sys.argv[1]).read().splitlines())
	nb_URLS = len(file)
	#print("\n".join(file))
	print 'nb_URLS dans le fichier',sys.argv[1],' : '+str(nb_URLS)
	
	file = [item for item in file if len(item) == 23 ]
	print 'nb_URLS apres suppression des liens trop courts : ',str(len(file))
	#print("\n".join(file))
	
	file=list(set(file))
	#print("\n".join(file))
	print 'nb_URLS apres suppression des doublons : ',str(len(file))
