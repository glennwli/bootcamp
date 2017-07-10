import gc

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f.seek(0)
    my_file = f.read()

file_header = my_file[:my_file.find('\n')]
my_sequence = my_file[my_file.find('\n')+1:]

my_sequence = my_sequence.replace('\n','')

print(gc.gc_map(my_sequence,1000,0.45))
