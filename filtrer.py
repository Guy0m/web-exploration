# Auteur : Guillaume Durupt
# Date : Decembre 2015
# Description : Filtrer les urls de tweets contenant un mot : 

import string
import csv
import re
import sys

class main:
	#print sys.argv[1]
	csv = csv.reader(open(sys.argv[1],"rb"))
	
	i=0
	nb_lignes=0
	liste=[]
	file1 = open("urls."+sys.argv[2]+".txt", "w")
  
	print "\nTraitement : \n"
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

	print 'nom.....',i,'/',nb_lignes,' tweets contenant  ',len(liste),' urls'
	file1.write("\n".join(liste))
	file1.close()
