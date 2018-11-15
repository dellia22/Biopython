#!/usr/bin/python

#CALCULATION OF GC CONTENT (GENES)

from Bio import SeqIO

import re

id_lista = []
id_=[]
#Crear dos listas y guardar en una los ids y en la otra las secuencias
file_name= '/home/DmdAnt/good_nt.fasta'
with open(file_name, "r") as f: #esta forma de abrir el archivo hace que no haga falta cerrar
    for line in f:
	line = line.strip() 
	if line.startswith('>'):
        	id_.append(str(line)) 
		s=0
	if line[0] != '>':
		id_lista.append(str(line))
		j=0

#Save ID in the file result_id
output_file= open('result_id.fasta', 'w')		
for y in id_:
	s+=1
	#print(str(s)+ y)
	output_file.write(str(s) + "\t" + y[1:] + "\n")

output_file.close()

#Save the GC content estimated in the file result_GC
output_file2= open('result_GC.fasta', 'w')
for x in id_lista:
	j+=1
	a=x.count('A')
	c=x.count('C')
	g=x.count('G')
	t=x.count('T')
	#print (str(j) + "\t" + str(float(c+g)/(a+c+g+t)))
	output_file2.write(str(j) + "\t" + str(float(c+g)/(a+c+g+t)) + "\n")

output_file2.close()

	
