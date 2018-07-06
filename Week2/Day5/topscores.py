def sort_scores(scores, highest):
    count = {}
    for x in scores:
        sc = count.get(x, 0)
        count[x] = sc + 1
    sort = []
    for i in range(highest + 1):
        if i in count:
            t = [i] * count[i]
            sort.extend(t)
    return list(reversed(sort))