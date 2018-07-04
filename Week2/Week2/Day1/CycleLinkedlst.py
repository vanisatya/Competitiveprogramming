def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    L1=first_node
    L2=first_node
    while(L1!=None and L2!=None and L2.next!=None ):
        L1=L1.next
        L2=L2.next.next
        if(L1==L2):
            return True

    return False