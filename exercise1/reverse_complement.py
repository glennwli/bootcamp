def complement(base, material = 'DNA'):
    """This makes a complement of each base"""
    # we will use this to complement each base individually
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'UuTt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'

def reverse_complement(seq, material = 'DNA'):
    """takes the sequence and retruns each complement, inreverse"""

    #initialize reverse
    rev_complement = ''

    for base in seq[::-1]:
        rev_complement += complement(base)

    return rev_complement

def display(seq):
    """"print and formats things nicely"""

    #print the sequence
    print(seq.upper())

    #print the spacers
    for base in seq:
        print ('|', end='')

    print ('')

    #print the reverse_complement
    print(reverse_complement(seq))
