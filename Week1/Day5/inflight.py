import unittest


def can_two_movies_fill_flight(ml, fl):

   
    lst=[]
        
    for i in range(len(ml)):
        add=0
        for j in range(i+1,len(ml)):
            add=ml[i]+ml[j]
               
            lst.append(add)
    
    
    q=check(lst,fl)

    
    return q
def check(array,fl1):
    
    for i in array:
        if i==fl1:
            return True
    return False