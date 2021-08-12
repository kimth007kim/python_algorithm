import sys

input = sys.stdin.readline

left =list(input().strip())
right = []
n=int(input())
for i in range(n):
    tmp = input().strip()
    if tmp[0]=="P":
        left.append(tmp[2])
    elif tmp=="L":
        if len(left)!=0:
            right.append(left.pop())
    elif tmp=="D":
        if len(right)!=0:
            left.append(right.pop())
    elif tmp=="B":
        if len(left)!=0:
            left.pop()

print("".join(left+ list(reversed(right))))