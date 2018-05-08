#!/usr/bin/env python3

import subprocess, re, os
from Bio import SeqIO
from Bio import AlignIO

regex = re.compile('[^A-Z]')

nameoffile="sequence" #archivo de entrada para 

records = list(SeqIO.parse(nameoffile, "fasta"))
numberofsequeces=len(records)			
print; input(str(numberofsequeces)+" total sequences. ")
lennumberofsequeces=len(str(numberofsequeces))
print; lennumberofsequeces

handle = open(nameoffile, "r")
filetowrite = open("sequences.fasta", "w")		
filetowrite2 = open("sequencesLongLabels.fasta", "w")	
j=0
for i in SeqIO.parse(handle, "fasta"):
	#if len(str(i.seq))<=500 and len(str(i.seq))>=400: # DddP
	j+=1
	print; i.name
	filetowrite.write(">"+"0"*(lennumberofsequeces-len(str(j)))+str(j)+"_seq"+"\n")
	filetowrite2.write(">"+"0"*(lennumberofsequeces-len(str(j)))+str(j)+"_"+str(i.description)+"\n")
	filetowrite.write(regex.sub("", str(i.seq).upper())+"\n")
	filetowrite2.write(regex.sub("", str(i.seq).upper())+"\n")
filetowrite2.close()
filetowrite.close()
handle.close()

records = list(SeqIO.parse("sequencesLongLabels.fasta", "fasta"))
numberofsequeces=len(records)
print; input(str(numberofsequeces)+" total sequences. ")
lennumberofsequeces=len(str(numberofsequeces))
print; lennumberofsequeces

subprocess.getoutput("rm alignment.fasta")
subprocess.getoutput("rm *.html")

print; "muscle -in sequences.fasta -out sequences.fasta.aln"
os.system("muscle -in sequences.fasta -out sequences.fasta.aln") #comandos para el alineamiento

print; "Launching trimAl..."
results=subprocess.getoutput("/home/gonzalez/Documents/trimal/source/trimal -in sequences.fasta.aln -fasta -automated1 -resoverlap 0.55 -seqoverlap 60 -out alignment.fasta -htmlout output.html")
print; results		#lanza trimAl para eliminar variabilidad despues del alineamiento

input_handle = open("alignment.fasta", "rU") 
output_handle = open("alignment.phylip", "w") #tipo de formato en el que se da el alineamiento
 
alignments = AlignIO.parse(input_handle, "fasta")
AlignIO.write(alignments, output_handle, "phylip")
 
output_handle.close()
input_handle.close()

print; "cp alignment.phylip"
results=subprocess.getoutput("cp alignment.phylip"); print; results

print; "cp sequencesLongLabels.fasta"
results=subprocess.getoutput("cp sequencesLongLabels.fasta"); print; results

records = list(SeqIO.parse("sequencesLongLabels.fasta", "fasta"))
numberofsequeces=len(records)
print; str(numberofsequeces)+" total sequences."

print; "I'm done!"

