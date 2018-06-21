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
filetoread = open("ID.txt", "r")
filetowrite = open("ID_specie_entrez.txt", "w")
lista = []
for line in filetoread:
	if len(line) > 0:
		line1 = line.split("\n")
		line1 = line1[0]
		lista.append(str(line1))
id_ = []
for x in lista:
	handle = Entrez.efetch(db = "nucleotide", id = x, retmode="xml")
	record = Entrez.read(handle)
	record2 = record[0]["GBSeq_definition"]
	id_.append(str(record2))
	#print (id_[0])
	output = set()


	for y in id_:
		output = set()
		output.add(y)
	for _ in output:
		print(_)

	filetowrite.write(str(_) + "\n")
		
filetoread.close()
filetowrite.close()










