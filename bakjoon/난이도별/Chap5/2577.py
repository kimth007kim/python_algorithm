in1 = int(input())
in2 = int(input())
in3 = int(input())

num = in1 * in2 * in3
a = num
nlist=[]
n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in range(10):
    b = a % 10
    a = a // 10
    nlist.append(b)
    if a<10:
        b=a
        nlist.append(b)
        break

for i in nlist:
    if i == 0:
        n0 += 1
    elif i == 1:
        n1 += 1
    elif i == 2:
        n2 += 1
    elif i == 3:
        n3 += 1
    elif i == 4:
        n4 += 1
    elif i == 5:
        n5 += 1
    elif i == 6:
        n6 += 1
    elif i == 7:
        n7 += 1
    elif i == 8:
        n8 += 1
    else:
        n9 += 1

print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)