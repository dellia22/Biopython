#!/usr/bin/python3

import sys

import os

from Bio import Entrez


Entrez.email = "dellia222@yahoo.es"
if not Entrez.email:
	print ("you must add your email address")

"""to get data from ncbi taxomomy, we need to have the taxid. we can
    get that by passing the species name to esearch, which will return
    the tax id"""

#para una lista de generos
filetoread = open("genero_list.txt", "r")
filetowrite = open("linage.txt", "w")
lista = []
for line in filetoread:
	if len(line) > 0:
		line1 = line.split("\n")
		line1 = line1[0]
		lista.append(str(line1))
id_ = []
for x in lista:
	search = Entrez.esearch(term = x, db = "Taxonomy")
	record = Entrez.read(search)
	record2 = record['IdList'][0]
	id_.append(str(record2))
	#print (id_[0])
	id2_ = []

	for y in id_:
		handle = Entrez.efetch(db="Taxonomy", id = y, retmode = "xml")
		records = Entrez.read(handle)
		records2 = records[0]["Lineage"]
		id2_.append(str(records2))
		output = set()
	for v in id2_:
		output = set()
		output.add(v)
	for _ in output:
		print(_)

	filetowrite.write(str(_) + "\n")
		
filetoread.close()
filetowrite.close()


#continua con el script parse_taxonomy_paso2.py







