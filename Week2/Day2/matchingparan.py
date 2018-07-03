def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    pc = 0
    l = len(sentence)
    for i in range (opening_paren_index+1,l):
        if(sentence[i]=='('):
            pc+=1;
        elif(sentence[i]==')'):
            if(pc == 0):
                return i
            else:
                pc-=1

    raise Exception