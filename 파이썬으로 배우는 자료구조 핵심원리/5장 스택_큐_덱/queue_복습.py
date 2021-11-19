class Queue:
    def __init__(self):
        self.container=list()

    def is_empty(self):
        if not self.container:
            return True
        else:
            return False
    def enqueue(self,data):
        self.container.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.container.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.container[0]

q= Queue()
q.enqueue(1)
q.enqueue(2)
print(q.container)
print(q.peek())
print(q.dequeue())
print(q.container)
