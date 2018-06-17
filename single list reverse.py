a = [0,1,2,3,4,5,6,7,8,9,10,11,12]
def reverselist(z):
    x = len(z)
    x = x-1
    y = 0
    if x/2 == 0:
        c = x/2
        c=c+1
    else:
        c = (x+1)/2
        c = c-1
    while x>c:
        b = a[y]
        z[y] = z[x]
        z[x] = b
        x=x-1
        y=y+1
    print z

reverselist(a)