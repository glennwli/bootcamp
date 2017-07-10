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

    big_seq = seq.upper()

    if material == 'DNA':
        A_rev = big_seq.replace('A','t')
    elif material == 'RNA':
        A_rev = big_seq.replace('A','u')

    C_rev = A_rev.replace('C','g')
    G_rev = C_rev.replace('G','c')
    T_rev = G_rev.replace('T','a')
    U_rev = T_rev.replace('U','a')

    return U_rev.upper()


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
