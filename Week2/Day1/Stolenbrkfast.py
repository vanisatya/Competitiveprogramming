def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    r = delivery_ids[0]
    l = len(delivery_ids)
    for i in range(1,l):
        r = r ^ delivery_ids[i]
    return r