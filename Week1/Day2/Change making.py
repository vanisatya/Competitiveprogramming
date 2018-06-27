import unittest


def change_possibilities(amount, denominations):
    a=amount
    l=list(denominations)
    m=len(denominations)
    k=count(l,m,a)
    return k

def count(l, m, a ):
 

    if (a== 0):
        return 1
 

    if (a < 0):
        return 0;
 
 
    if (m <=0 and a >= 1):
        return 0
 
   
    return count( l, m - 1, a ) + count( l, m, a-l[m-1] );
    

