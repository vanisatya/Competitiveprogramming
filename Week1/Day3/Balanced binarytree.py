leaf = 0
def is_balanced(root):
    result = checkBalanced(root)
    return result
def height(root):
    global leaf
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        leaf+=1
    return max(height(root.left), height(root.right)) + 1
def checkBalanced(root):
    if root is None:
        return True
    global leaf
    leaf = 0
    leftHeight = height(root.left)
    rightHeight = height(root.right) 
    if (abs(leftHeight - rightHeight) <= 1) and checkBalanced(root.left) is True and checkBalanced( root.right) is True:
        return True
    if leaf == 1:
        return True
    return False
