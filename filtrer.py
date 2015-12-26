# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Description : Filtrer les urls de tweets contenant un mot 
# Utilisation :  filtrer.py tweets.csv nomafiltrer

import string
import csv
import re
import sys
import os

class main:

	csv = csv.reader(open(sys.argv[1],"rb"))
	i=0
	nb_lignes=0
	liste=[]
	file = open("URLs."+sys.argv[2]+".txt", "w")
  
	print "\nFiltrer : \n"
	for row in csv:
		nb_lignes=nb_lignes+1
			
		regex=re.compile(sys.argv[2],re.IGNORECASE) 
		nom=regex.search(row[0])
		if nom:
			i=i+1
			url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', row[0])
			if url:
				for elem in url: #un tweet peut contenir plusieurs urls
					liste.append(elem)	 

	print 'Nombre de tweets contenant "'+sys.argv[2]+'".....',i,'/',nb_lignes,'\nNombre d\'URLs extraites  .................',len(liste)
	print '\nResultat : '+ file.name
	file.write("\n".join(liste))
	file.close()
