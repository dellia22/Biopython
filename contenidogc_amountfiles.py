#!/usr/bin/python

#CALCULATION OF GC CONTENT (GENES)

from Bio import SeqIO

import re

import glob

import errno

import os, sys
from os import getcwd

import commands, os, re, fnmatch

id_lista = []
id_=[]

cwd = '/home/gonzalez/Documentos/laura/Evolution_DmdA/EvolutionDmdA_BactMAR/DATABASE/'
genomes = os.listdir(cwd)
for filename in genomes:
	with open(os.path.join(cwd, filename), 'rb') as fh:
		for line in fh:
			line=line.strip()
#			print(line)
			if line.startswith('>'):
     				id_.append(str(line)) 
				s=0
				output_file= open('result_id'+filename+'.fasta', 'w')
				for y in id_:
					s+=1
					output_file.write(str(s)+ "\t" + y[1:] + "\n") 
			if line[0] != '>':
				id_lista.append(str(line))
				j=0
				output_file2=open('result_GC'+filename+'.fasta', 'w')
				for x in id_lista:
					j+=1
					a=x.count('A')
					c=x.count('C')
					g=x.count('G')
					t=x.count('T')

					output_file2.write(str(j) + "\t" + str(float(c+g)/(a+c+g+t)) + "\n")

output_file.close()
output_file2.close()
