class Stack:
    def __init__(self):
        self.container =list()

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
        return self.container.pop()

    def peek(self):
        if self.empty():
            return None
        return self.container[-1]

    def __str__(self):
        return "{}".format(self.container)

s= Stack()


s.push(1)
print(s)
s.push(2)
print(s)
s.push(3)
print(s)
s.push(4)
print(s)
s.push(5)
print(s)

while not s.empty():
    print(s.pop(),end="")
    print(s)

