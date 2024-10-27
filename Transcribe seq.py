'''
Title: Read the “cds_seq.fasta” file and transcribe the sequence in the FASTA file.
Save the transcribed mRNA sequence in another FASTA file (mRNA_seq.fasta).
'''

# import packages
from Bio.Seq import Seq

# read mRNA_seq.fasta file
with open("cds_seq.fasta","r") as file2:
    sequence= ""
    for lines in file2:
        lines = lines.strip()
        # store the fasta header in header variable
        if ">" in lines:
            header = lines
        else:
            # transcribe the sequence
            # sequence = Seq(lines)
            # mrna = sequence.transcribe()
            # mrna = str(mrna)
            sequence += lines
            mrna = sequence.replace("T","U")

# save the transcribed sequence in a new fasta file.
f = open("mRNA_seq.fasta", "w")
f.write(header + ".transcribed\n" + mrna)
f.close()
