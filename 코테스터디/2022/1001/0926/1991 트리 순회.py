from collections import defaultdict
import sys

input =sys.stdin.readline

class Node:
    def __init__(self, value):
        if value==".":
            return
        self.left = None
        self.right = None
        self.value = value
    def left(self,left):
        self.left=left
    def right(self,right):
        self.right=right

def preorder(node):
    if node:
        preanswer.append(node.value)
        if node.left:
            preorder(tree[node.left.value])
        if node.right:
            preorder(tree[node.right.value])

def postorder(node):
    if node:
        if node.left:
            postorder(tree[node.left.value])
        postanswer.append(node.value)
        if node.right:
            postorder(tree[node.right.value])
def inorder(node):
    if node:
        if node.left:
            inorder(tree[node.left.value])
        if node.right:
            inorder(tree[node.right.value])
        inanswer.append(node.value)

n = int(input())
tree=defaultdict(Node)
for i in range(n):
    p, a, b = map(str, input().rstrip().split())
    parent=Node(p)
    tree[p]=parent
    if a!=".":
        left=Node(a)
        tree[a]=left
        parent.left=left
    if b!=".":
        right=Node(b)
        tree[b]=right
        parent.right=right
preanswer=[]
postanswer=[]
inanswer=[]
preorder(tree["A"])
postorder(tree["A"])
inorder(tree["A"])
print("".join(preanswer))
print("".join(postanswer))
print("".join(inanswer))