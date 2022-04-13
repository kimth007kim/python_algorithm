from collections import defaultdict

n= int(input())
dic=defaultdict(list)
for i in range(n):
    p,c1,c2= input().split()
    # if c1 != ".":
    dic[p].append(c1)
    # if c2 != ".":
    dic[p].append(c2)
# print(dic)
def preorder(now):
    if now != ".":
        print(now,end="")
        preorder(dic[now][0])
        preorder(dic[now][1])

def inorder(now): #중위 순회
    if now != ".":
        inorder(dic[now][0])
        print(now, end="")
        inorder(dic[now][1])

def postorder(now):
    if now != ".":
        postorder(dic[now][0])
        postorder(dic[now][1])
        print(now, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
