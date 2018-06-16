a = [0,1,2,3]
def reverselist(x):
    b = len(x)
    b = b-1
    c = 0
    d = []
    while b >-1:
        d.insert(c,x[b])
        b = b-1
        c = c+1
    print d


reverselist(a)