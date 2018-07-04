def reverse_words(message):
    l = len(message)
    message = reverse(message,0,l)
    i=0
    while(i<l):
        st = i
        while(i<l and message[i]!=' '):
            i+=1
        en = i
        message = reverse(message,st,en)
        i+=1
    return message

def reverse(list_of_chars, st, en):
    limit = st + (en-st)/2
    for i in range (st,limit):
        (list_of_chars[i], list_of_chars[st+en-i-1] ) = (list_of_chars[st+en-i-1], list_of_chars[i])
    return list_of_chars

