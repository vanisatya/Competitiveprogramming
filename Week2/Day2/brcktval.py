def is_valid(code):

    # Determine if the input code is valid
    Bracket = []
    for i in code:
        if(i=='(' or i=='[' or i=='{'):
            Bracket.append(i)
        else:
            if(len(Bracket)>0):
                check = Bracket.pop()
                if(ord(i)-ord(check)!=1 and ord(i)-ord(check)!=2 ):
                    return False
            else:
                return False

    if(len(Bracket)==0):
        return True
    else:
        False
