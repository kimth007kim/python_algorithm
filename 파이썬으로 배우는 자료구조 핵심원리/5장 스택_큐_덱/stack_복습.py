class Stack:
    def __init__(self):
        self.container=list()
    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self,data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        else:
            return self.container.pop()

    def peek(self):
        if self.empty():
            return None
        else:
            return self.container[-1]


s= Stack()
s.push(1)
print(s.container)
s.push(2)
print(s.container)
print(s.peek(4444444444444444444444444444444444))
print(s.container)
