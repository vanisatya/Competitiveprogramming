def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list
    i = 0
    kth = head
    while(head and head.next):
        head = head.next
        if i == k - 1:
            kth = kth.next
        else:
            i += 1
            
    if i != k-1 or k is 0:
        raise ValueError("K is not in the limits")
    return kth

