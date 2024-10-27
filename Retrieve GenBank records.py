'''
Title:  A Python script to retrieve the GenBank records
Author: Dinuri Vishara
Date: 05/03/2023
'''

# import packages
from Bio import Entrez,SeqIO
Entrez.email = "dinurilokuwalpola1998@gmail.com"

# create a list of accession numbers
idlist = ["AAK43967.1","AED90870.1","NP_567720.1","AAK59861.1"]

for id in idlist:
    handle = Entrez.efetch(db="protein", id=id , rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    SeqIO.write(record, f"{id}.fasta" , "fasta")