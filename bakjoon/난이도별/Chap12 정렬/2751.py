import sys
n= int(sys.stdin.readline())
slot=[]
for j in range(n):
    slot.append(int(sys.stdin.readline()))

slot.sort()
for k in slot:
    print(k)