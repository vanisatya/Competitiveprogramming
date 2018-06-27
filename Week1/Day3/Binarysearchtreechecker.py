import unittest


global arr
arr=[]
def inord(root):
    array1=inorderTraversal(root)
    return array1

def isAscending(x):
    if len(x)==1:
        return True
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            return False
    return True
def inorderTraversal(root):
    if root:
        inord(root.left)
        arr.append(root.value)
        inord(root.right)
    return arr





def is_binary_search_tree(root):
    array2 = inord(root)
    q=isAscending(array2)
    global arr
    arr[:]=[]
    
    return q
    