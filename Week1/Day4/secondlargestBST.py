import unittest
global array
array=[]

def inorderTraversal(root):
    if root:
        inorder(root.left)
        array.append(root.value)
        inorder(root.right)
    return array
def secondLargest(x):
    if len(x)>1:
        return x[len(x)-2]
    else:
        raise IndexError("Mininmum of 2 elements are required")
def inorder(root):
    arr1=inorderTraversal(root)
    return arr1

def find_second_largest(root):
    arr2 = inorder(root)
    q=secondLargest(arr2)
    global array
    array[:]=[]
    
    return q