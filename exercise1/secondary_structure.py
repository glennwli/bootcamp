def validate_par (structure):
    """makes sure number of open = number of closed"""

    if structure.count('(') == structure.count(')') and structure.find('(')<structure.find(')'):
        return True

    return False

def dotparen_to_bp(structure):
    """converts dot parens"""

    #check if valid
    if validate_par(structure) == False:
        return -1

    open_coord = []
    basepairs = []

    for i, char in enumerate(structure):
        if char == '(':
            open_coord.append(i)
        elif char ==')':
            if len(open_coord)>0:
                basepairs.append((open_coord.pop(),i))
            else:
                return -1
    return tuple(sorted(basepairs))


def verify_hairpin(structure):
    """check validity of hairpins"""
    #get basepairs
    basepairs = dotparen_to_bp(structure)

    #make sure the structure was valid
    if basepairs == -1:
        return False

    #check that they're all at least 4 apart
    for bp in basepairs:
        if bp[0] + 4 >= bp[1]:
            return False

    return True

def rna_ss_validator(seq, sec_struc, wobble=True):
    """checks 2' struct"""

    #check if same length, hairpins and sec_struc input are valid

    if not(verify_hairpin(sec_struc) and validate_par(sec_struc)
    and len(seq)==len(sec_struc)):
        return False

    #get base pairs
    bp_position = dotparen_to_bp(sec_struc)


    #valid pairs
    if wobble:
        valid = ('gu','gc','au','ug','cg','ua')
    else:
        valid = ('gc','au','ug','cg','ua')


    for i, bp in enumerate(bp_position):
        basepair = (seq[bp[0]]+seq[bp[1]]).lower()

        if basepair not in valid:
            return False

    #if we made it this far, we're true
    return True
