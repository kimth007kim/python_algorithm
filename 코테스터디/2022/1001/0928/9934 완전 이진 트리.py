from collections import defaultdict, deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def treeNode(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    if arr[mid] in tree:
        now = tree[arr[mid]]
    else:
        now = Node(arr[mid])
        tree[arr[mid]] = now
    now.left = treeNode(arr[:mid])
    now.right = treeNode(arr[mid + 1:])
    return now


tree = defaultdict(Node)
n = int(input())
arr = list(map(int, input().split()))
level = defaultdict(list)
root = arr[len(arr) // 2]
q = deque()

treeNode(arr)
visited = [0] * (len(arr) + 1)
q.append([root, 0])
idx = set()
while q:
    val, lv = q.popleft()
    idx.add(lv)
    now = tree[val]
    # print(now, lv)
    level[lv].append(val)
    if now.left != None:
        q.append([now.left.value, lv + 1])
    if now.right != None:
        q.append([now.right.value, lv + 1])

idx = list(idx)
idx.sort()
for i in idx:
    print(*level[i])