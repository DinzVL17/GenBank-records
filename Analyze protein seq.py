'''
Title: Read the “aa_seq.fasta” and analyze the sequence.
Calculate the length, molecular weight, alanine percentage, and glycine percentage of the sequence.
Save the calculated parameters in a new text file called “aa_stats.txt”.
'''

# import packages
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# read the fasta file with translated sequence
with open("aa_seq.fasta","r") as file4:
    for lines in file4:
        lines = lines.strip()
        # calculate the length, molecular weight, alanine percentage,
        # and glycine percentage of the sequence
        if ">" not in lines:
            # store the translated sequence in sequence variable
            sequence=""
            # replace specific characters
            sequence += lines.replace("*","")
            # get the length of the sequence
            length = len(sequence)

            seq = ProteinAnalysis(sequence)

            # calculate the length, molecular weight, alanine percentage,
            # and glycine percentage of the sequence
            alanine_percentage = seq.get_amino_acids_percent()["A"]
            glycine_percentage = seq.get_amino_acids_percent()["G"]
            moleculr_weight = seq.molecular_weight()

# Save the calculated parameters in a new text file
with open("aa_stats.txt",'w') as file5:
    file5.write("Length of the sequence:%.3f" %length)
    file5.write("\n")
    file5.write("Alanine percentage:%.3f" %alanine_percentage)
    file5.write("\n")
    file5.write("Glycine percentage:%.3f" %glycine_percentage)
    file5.write("\n")
    file5.write("Molecular weight:%.3f" %moleculr_weight)

