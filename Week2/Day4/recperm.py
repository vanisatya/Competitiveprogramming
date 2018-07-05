def get_permutations(string):

    # Generate all permutations of the input string
    s = []
    l = len(string)
    if(l==0 or l==1):
        return set([string])
    for i in range (l):
        newstring = string[0:i]+string[i+1:l]
        nl = get_permutations(newstring)
        for k in nl:
            s.append(string[i]+k)
    return set(s)

