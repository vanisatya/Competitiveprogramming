
def unboundedKnapsack(caketup, p, n):
    k=[0]*(p+1)
    for i in range(p + 1):
        for j in range(n):
            if (caketup[j][0] <= i):
                k[i] = max(k[i], k[i - caketup[j][0]] + caketup[j][1])

    return k[p]
def max_duffel_bag_value(caketup, weightcap):
    for cake in caketup:
        if (cake[0] == 0 and cake[1] != 0):
            return float('inf')
    n = len(caketup)
    return unboundedKnapsack(caketup, weightcap, n)
    return -1
