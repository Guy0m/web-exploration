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
	liste = list(open(sys.argv[1]).read().splitlines())
	nb_URLS = len(liste)
	#print("\n".join(liste))
	print 'nb_URLS dans le fichier',sys.argv[1],' : '+str(nb_URLS)
	
	liste = [item for item in liste if len(item) == 23 ]
	print 'nb_URLS apres suppression des liens trop courts : ',str(len(liste))
	#print("\n".join(liste))
	
	liste=list(set(liste))
	#print("\n".join(liste))
	print 'nb_URLS apres suppression des doublons : ',str(len(liste))
	
	file = open("URLs.clean."+sys.argv[1]+".txt", "w")
	print '\nResultat : '+ file.name
	file.write("\n".join(liste))
	file.close()
