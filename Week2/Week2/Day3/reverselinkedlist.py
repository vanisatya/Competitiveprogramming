def reverse(head_of_list):
    prev = None
    current = head_of_list
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head_of_list = prev
    return prev