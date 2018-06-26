def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Minimum 2 numbers are required to get the product ')
    products = [None] * len(int_list)
    product = 1
    for i in xrange(len(int_list)):
        products[i] = product
        product*= int_list[i]
    product = 1
    for i in xrange(len(int_list) - 1, -1, -1):
        products*= product
        product*= int_list[i]

    return products

    return []