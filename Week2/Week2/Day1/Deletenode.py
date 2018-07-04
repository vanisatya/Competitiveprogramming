def delete_node(node_to_delete):

    # Delete the input node from the linked list
    k = node_to_delete.next.value
    node_to_delete.next = node_to_delete.next.next
    node_to_delete.value = k
