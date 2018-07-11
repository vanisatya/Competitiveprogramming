def find_duplicate(list):
    num = len(list)
    x = num
    y = num
    while True:
        x = list[x - 1]  # slow
        y = list[y - 1]  # fast
        y = list[y - 1]  # fast
        if x == y:
            break
    y = num
    while True:
        x = list[x - 1]
        y = list[y - 1]
        if x == y:
            break
    return x


