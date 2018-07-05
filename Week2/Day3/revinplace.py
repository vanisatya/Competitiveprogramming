def reverse_bytes_in_place(l):

    a = len(l)
    for i in range(a / 2):
        (l[i], l[a - i - 1]) = (l[a - i - 1], l[i])
    return l


def  reverse(string):
    x = reverse_bytes_in_place(string)

    return x
