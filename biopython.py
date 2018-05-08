#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:42:24 2018

@author: usuario
"""


from Bio import SeqIO

id_lista = []
file_name= '/home/usuario/Documentos/laura/Evolutionary_history/BLAST/ID_target_psiblast.fasta'
with open(file_name, "r") as f: #esta forma de abrir el archivo hace que no haga falta cerrar
    for line in f:
        line = line.strip() 
        id_lista.append(str(line))
	#for x in id_lista:
		#print (id_lista)

input_file = open('/home/usuario/Documentos/laura/Evolutionary_history/BLAST/file_WP_.txt', 'r')
output_file = open('result.fasta','a')
for key in SeqIO.parse(input_file, 'fasta'):
	entry_name = key.name
	if key.name in id_lista:
		output_file.write(str('>' + (key.id)) + '\n')
		output_file.write(str(key.seq[0:])+'\n')

output_file.close()
input_file.close()


