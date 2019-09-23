#!/usr/bin/env python

import subprocess, re, os
from Bio import SeqIO
from Bio import AlignIO


input_handle = open("alignment.fasta", "rU") 
output_handle = open("alignment.phylip", "w") #tipo de formato en el que se da el alineamiento
 
alignments = AlignIO.parse(input_handle, "fasta")
AlignIO.write(alignments, output_handle, "phylip")
 
output_handle.close()
input_handle.close()

results=subprocess.getoutput("cp alignment.phylip"); print (results)

