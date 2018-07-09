def is_single_riffle(half1, half2, shuffled_deck):

    # Check if the shuffled deck is a single riffle of the halves
    lh1 = len(half1)
    lh2 = len(half2)
    l = len (shuffled_deck)
    i = 0
    j = 0
    for x in range (l):
        if(i<lh1 and shuffled_deck[x] == half1[i]):
            i+=1
        elif(j<lh2 and shuffled_deck[x] == half2[j]):
            j+=1
        else:
            return False
    return True