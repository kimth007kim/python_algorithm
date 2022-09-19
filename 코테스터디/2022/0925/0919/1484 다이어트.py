import sys

input = sys.stdin.readline


n=int(input())

end=1
start=1
total=0
answer=set()
while start<=end and end<=10000000:
    total =end**2 - start**2
    if total==n:
        answer.add(end)
    while total<n:
        end+=1
        total = end ** 2 - start ** 2
        if total== n:
            answer.add(end)
    start+=1

result = list(answer)
result.sort()
if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)