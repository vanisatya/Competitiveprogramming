def has_palindrome_permutation(the_string):
    # Check if any permutation of the input is a palindrome
    l = len(the_string)
    dictn = {}
    for i in range (l):
        c = dictn.setdefault(the_string[i], 0)
        dictn[the_string[i]]=c+1
        
    if (l%2==0):
        for k in dictn.keys():
            if (dictn[k]%2!=0):
                return False
    else:
        flag = False
        for k in dictn.keys():
            if (dictn[k]%2!=0):
                if(flag == True):
                    return False
                else:
                    flag = True
    return True

