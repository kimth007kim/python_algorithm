
left = dict()
right = dict()

n = int(input())

parent = [0] * (n + 1)
node_count = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    left[a] = b
    right[a] = c

    if b != -1:
        parent[b] = a
        node_count += 1
    if c != -1:
        parent[c] = a
        node_count += 1

last_node = 0


def traverse(node):
    global last_node
    if node == -1:
        return
    traverse(left[node])
    last_node = node
    traverse(right[node])


traverse(1)
edge_count = node_count * 2
movement = 0

while last_node != 1:
    print(last_node)
    movement += 1
    last_node = parent[last_node]


print(edge_count -movement)

print(left)
print(right)