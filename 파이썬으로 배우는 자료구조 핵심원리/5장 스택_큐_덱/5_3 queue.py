class Queue:
    def __init__(self):
        self.container= list()

    def is_empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        self.container.pop(0)

    def peek(self):
        return self.container[0]

    def __str__(self):
        return "{}".format(self.container)


q= Queue()
print(q.is_empty())
print(q.peek)

# q.enqueue(123123)
print(q)