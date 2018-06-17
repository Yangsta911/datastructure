a = []
def queue(y):
    while True:
        z = raw_input('do you want to add or delete?:')
        if z == 'delete':
            if len(y) == 0:
                print 'error'
            else:
                t = y[0]
                y.remove(y[0])
                print t
        elif z == 'add':
            y.append(raw_input('add what:'))
        if z == 'stop':
            break
        print a
queue(a)