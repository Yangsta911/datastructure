x = 0
list = []
while x < 101:
    list.append(x)
    x=x+1
while True:
    number = raw_input("which index in the list: ")
    if number == 'stop':
        break
    if number>101:
        print 'error'
    elif number<1:
        print 'error'
    else:
        print list[number-1]
