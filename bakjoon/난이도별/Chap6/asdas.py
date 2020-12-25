a= 8763
n1 = a // 1000
n2 = (a - n1 * 1000) // 100
n3 = (a - n1 * 1000 - n2 * 100) // 10
n4 = a - n1 * 1000 - n2 * 100 - n3 * 10
res = a + n1 + n2 + n3 + n4

print(n1)
print(n2)
print(n3)
print(n4)
print(res)