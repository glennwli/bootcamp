import bioinfo_dicts as bd

def longest_orf(seq, number = 1):
    """finds the n longest ORF from a sequence"""

    seq = seq.upper()
    longest_orf = ''
    stop_codons = ['TAA','TGA','TAG']
    codon = ''
    orf_length = 0

    #initialize starting of the orf
    for i in range(0,len(seq)):

        #if we find a start codon
        if seq[i:i+3] == 'ATG':
            orf_length = 0
            codon = ''
            #add 3 to length while we're not a stop codon
            while codon not in stop_codons and i + orf_length < len(seq)-2:
                #a codon starts at i
                codon = seq[i + orf_length : i + orf_length + 3]
                orf_length += 3

        #if the orf we found is longer than the previous longest, get that seq
            if orf_length >= len(longest_orf):
                longest_orf = seq[i : i + orf_length]



    return longest_orf

def translate_orf(seq):
    """ translates DNA sequence to protein"""
    seq = seq.upper()
    #check that we have a valid orf
    if len(seq)%3 != 0:
        print ("invalid orf")
        return False

    protein = ''

    for i in range(0, len(seq), 3):
        protein += bd.codons[seq[i:i+3]]

    return protein

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f.seek(0)
    my_file = f.read()

file_header = my_file[:my_file.find('\n')]
my_sequence = my_file[my_file.find('\n')+1:]

my_sequence = my_sequence.replace('\n','')

print(longest_orf(my_sequence))
