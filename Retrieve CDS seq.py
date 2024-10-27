'''
Title: Retrieve the GenBank record for an accession number (with version) of a
protein coding DNA sequence or a reverse-transcribed mRNA complement
given by the user and save the sequence in FASTA format (cds_seq.fasta)
'''

# import packages
from Bio import Entrez

# get the accession number as a user input
accession_num = input("Enter the accession number:")

# retrieve the GenBank record for the given accession number
Entrez.email = "D.Vishara@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=accession_num, rettype="fasta", retmode="text")

#save the sequence in fasta format
with open("cds_seq.fasta","w") as file2:
    file2.write(handle.read())