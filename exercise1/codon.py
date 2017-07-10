codon = "UAA"
if codon == 'AUG':
    print("This is a start codon")
    print("indentaiton matters")
elif codon == "UAA":
    print("yeup")
else:
    print("this is not a start codon")
    if codon == "UAA" or codon == "UAG" or codon == "UGA":
        print("this is a stop codon")
    print("indentation still matters")
