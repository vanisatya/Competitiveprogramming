def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Minimum of 3 items are required')
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])
    h2 = list_of_ints[0] * list_of_ints[1]
    l2  = list_of_ints[0] * list_of_ints[1]
    h3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    for i in xrange(2, len(list_of_ints)):  
        current = list_of_ints[i]
        h3 = max(h3,current * h2,current *l2)
        h2 = max(h2,current * highest,current * lowest)
        l2 = min(l2,current * highest,current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current)

    return h3

    return 0

