import unittest
def contains(ordered_list, number):
    l=len(ordered_list)
    k=binarySearch(ordered_list,0,l-1,number)
    return k

def binarySearch(lst,low,high,a):
    
    while low<=high:
    
        k=(high+low)//2
        if lst[k]<a:
            low=k+1
        elif lst[k]>a:
            high=k-1
        else:
            return True
    return False