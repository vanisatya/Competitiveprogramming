import unittest
def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    res = []
    l1 = len(my_list)
    l2 = len(alices_list)
    x = 0
    y = 0
    
   
    while(x<l1 and y<l2):
        if(my_list[x]<alices_list[y]):
            res.append(my_list[x])
            x+=1
        else:
            res.append(alices_list[y])
            y+=1
    while(x<l1):
        res.append(my_list[x])
        x+=1
    while(y<l2):
        res.append(alices_list[y])
        y+=1
            
    
    
    
    return res




