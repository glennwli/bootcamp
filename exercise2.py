def gc_blocks(seq,block_size):
    """Splits a sequence into non-overlapping blocks
    and calculates each block's GC content"""

    block_gc = []

    for i in range(0, len(seq) - (len(seq)%block_size), block_size):
        block_gc.append(gc_content(seq[i:i+block_size]))

    return tuple(block_gc)


def gc_content(seq):
    """Calculates GC content of a given sequence"""
    seq = seq.upper()

    gc_content = (seq.count('G') + seq.count('C'))/len(seq)

    return gc_content

def gc_map(seq, block_size, gc_threshold):

    block_gc = gc_blocks(seq,block_size)

    mapped_seq = ''

    for i, gc in enumerate(block_gc):
        if gc <= gc_threshold:
            mapped_seq += seq[i * block_size:(i+1) * block_size].lower()
        else:
            mapped_seq += seq[i * block_size:(i+1) * block_size].upper()

    return mapped_seq

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f.seek(0)
    my_file = f.read()

file_header = my_file[:my_file.find('\n')]
my_sequence = my_file[my_file.find('\n')+1:]

my_sequence = my_sequence.replace('\n','')

my_map = gc_map(my_sequence,1000,0.45)

with open('exercise2_out.fna','w') as f_out:
    f_out.write(file_header + '\n')
    for i in range(0, len(my_map), 60):
        f_out.write(my_map[i:i+60]+'\n')
