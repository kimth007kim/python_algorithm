class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class linked:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.now = None

        self.stack = []

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_back(self, new_node):

        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def find_now(self, k):
        cur = self.head.next
        cnt = 0
        while k > cnt:
            cur = cur.next
            cnt += 1
        self.now = cur

    def delete(self):
        self.stack.append([self.now.prev.data, self.now.data, self.now.next.data])

        if self.now.next == self.tail:
            self.now.prev.next = self.now.next
            self.now.next.prev = self.now.prev
            self.now = self.tail.prev
        else:
            self.now.prev.next = self.now.next
            self.now.next.prev = self.now.prev
            self.now = self.now.next

    def move(self, command, number):
        cnt = 0
        tmp = int(number)
        cur = self.now
        while cnt < tmp:
            if command == "U":
                cur = cur.prev
            else:
                cur = cur.next
            cnt += 1
        self.now = cur

    def undo(self, dict):
        t_prev, t_now, t_next = self.stack.pop()
        if t_prev == None:
            previous = self.head
        else:
            previous = dict[t_prev]
        if t_next == None:
            nextOne = self.tail
        else:
            nextOne = dict[t_next]
        new_node = dict[t_now]

        previous.next = new_node
        nextOne.prev = new_node

        new_node.next = nextOne
        new_node.prev = previous


def solution(n, k, cmd):
    answer = ["X"] * n
    dlist = linked()
    dict = {}
    # 링크드리스트탐색 속도를 올리기위해 딕셔너리 사용

    for i in range(n):
        new_node = Node(i)
        dict[i] = new_node
        dlist.add_back(new_node)

    dlist.find_now(k)
    for i in cmd:
        if len(i) == 1:
            if i == "C":
                dlist.delete()
            else:
                dlist.undo(dict)
        else:
            command, number = i.split()
            dlist.move(command, number)

    cur = dlist.head.next
    while cur != dlist.tail:
        answer[cur.data] = "O"
        cur = cur.next

    return "".join(answer)