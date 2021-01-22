n=int(input())
number=[]
for i in range(n):
    number.append(int(input()))

number= sorted(number,reverse=True)
for j in number:
    print(j,end=" ")