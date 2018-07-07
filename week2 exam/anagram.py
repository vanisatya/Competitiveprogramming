x=" SiLeNt CAT"
y=" LisTen AcT"
def anagram(x,y):
    t=x.upper()
    s=y.upper()
    tl = len(t)
    sl = len(s)
    ts = sorted(t)
    ss=  sorted(s)
    print(ts)
    print(ss)
    
    for i in range(0, tl):
        if(ts[i]==' '):
            ts[i].remove()
        if(ss[i]==' '):
            ss[i].remove()
        if(ts[i]!=ss[i]):
            return False
    return True

print(anagram(x,y))
