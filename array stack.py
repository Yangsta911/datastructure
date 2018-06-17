a = []
def arraystack(y):
    while True:
        z = raw_input('do you want to pop or push?:')
        if z == 'pop':
            if len(y) == 0:
                print 'error'
            else:
                t = y[x]
                y.remove(y[x])
                print t
        elif z == 'push':
            y.append(raw_input('push what:'))
        if z == 'stop':
            break
        x = len(y)
        x = x - 1
        print a
arraystack(a)