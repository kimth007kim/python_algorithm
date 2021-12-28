class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class linked:
    def __init__(self, k):
        self.head = Node()
        self.tail = Node()
        self.now = None

        self.stack = []

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_back(self, data):
        new_node = Node(data)

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
        # print("-------------------------")
        # print("C: 삭제 그리고 바로 아래행 이미 가장아래이면 바로 윗행 선택")
        self.stack.append([self.now.prev.data, self.now.data, self.now.next.data])

        if self.now.next == self.tail:
            self.now.prev.next = self.now.next
            self.now.next.prev = self.now.prev
            self.now = self.tail.prev
        else:
            self.now.prev.next = self.now.next
            self.now.next.prev = self.now.prev
            self.now = self.now.next

    #             print("꼬리아님")

    #         print(self.stack)
    #         print("현위지 = ",self.now.data)
    #         print("-------------------------")

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

    def undo(self):
        t_prev, t_now, t_next = self.stack.pop()
        previous = self.head
        nextOne = self.tail
        while t_prev != previous.data:
            previous = previous.next

        while t_next != nextOne.data:
            nextOne = nextOne.prev

        new_node = Node(t_now)
        previous.next = new_node
        nextOne.prev = new_node
        new_node.next = nextOne
        new_node.prev = previous

        # print(self.stack)


def show_list(dlist):
    cur = dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end="  ")
        cur = cur.next


def solution(n, k, cmd):
    answer = ["X"] * n
    dlist = linked(k)
    for i in range(n):
        dlist.add_back(i)

    dlist.find_now(k)
    for i in cmd:
        if len(i) == 1:
            if i == "C":
                dlist.delete()
            else:
                dlist.undo()
        else:
            command, number = i.split()
            dlist.move(command, number)

    cur = dlist.head.next
    while cur != dlist.tail:
        answer[cur.data] = "O"
        cur = cur.next

    return "".join(answer)