class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

s = Stack()
while True:
    z = raw_input('do you want to pop or push:')
    if z == 'push':
        a = raw_input('what do you want to push:')
        s.push(a)
    if z == 'pop':
        if s.isEmpty() == True:
            print 'error'
        else:
            print (s.pop())
    if z == 'stop':
        break