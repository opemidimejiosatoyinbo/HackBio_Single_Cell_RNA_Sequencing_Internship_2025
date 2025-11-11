"""
HackBio Internship - Stage 1 Python Task
Team: Glycine

# Task: Write a Python function for translating DNA to protein
# Author: Opemidimeji Osatoyinbo
# GitHub: https://github.com/opemidimejiosatoyinbo
# LinkedIn: https://linkedin.com/in/opemidimejiosatoyinbo
"""
# Standard codon table (DNA -> amino acid single-letter)
CODON_TABLE = {
    'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
    'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
    'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
    'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
    'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
    'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
    'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
    'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
    'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
    'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
    'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
    'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
    'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
    'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
    'TAC':'Y','TAT':'Y','TAA':'_','TAG':'_',
    'TGC':'C','TGT':'C','TGA':'_','TGG':'W'
}

def dna_to_protein(dna_sequence: str) -> str:
    """
    Translate a DNA sequence to a protein sequence.

    Parameters
    ----------
    dna_sequence : str
        String of DNA bases (A, T, C, G). Whitespace is ignored; case-insensitive.

    Returns
    -------
    str
        Protein sequence (one-letter codes). Unknown codons -> 'X'.
    """
    seq = dna_sequence.upper().replace(" ", "")
    protein = []
    # iterate in steps of 3, ignore trailing incomplete codon
    for i in range(0, len(seq) - (len(seq) % 3), 3):
        codon = seq[i:i+3]
        protein.append(CODON_TABLE.get(codon, 'X'))
    return "".join(protein)


if __name__ == "__main__":
    # Example sequence (you can replace with any sequence)
    example = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    print("DNA sequence:", example)
    print("Translated protein:", dna_to_protein(example))