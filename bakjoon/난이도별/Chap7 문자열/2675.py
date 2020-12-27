S =int(input())
numlist=[]
for i in range(S):
    result = ""
    a,b = input().split()
    a= int(a)
    blen= len(b)
    for i in range(blen):
        result+= b[i]*a
    numlist.append(result)

for i in range(S):
    print(numlist[i])