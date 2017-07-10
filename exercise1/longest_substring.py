def longest_substring(seq1,seq2):
    """finds the longest substring"""

    if len(seq1)<len(seq2):
        seq1,seq2 = seq2,seq1
        
    #initialize longest, stores length of the longest
    longest = 0

    #interate through seq1, check each length in seq1
    for i in range(len(seq1)):
        for j in range(len(seq1)-i+1):
            if seq1[i:j+i] in seq2 and j+1>longest:
                longest = j+1
                longest_string = seq1[i:i+j]
                print(longest_string)


    return longest_string
