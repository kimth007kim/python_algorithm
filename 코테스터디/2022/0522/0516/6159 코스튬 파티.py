n,s = map(int,input().split())
data=[]
for i in range(n):
    data.append(int(input()))
answer=0
data.sort()
start=0
end=n-1

for start in range(n-1):
    end=start+1
    while start<end and end<n:
        _sum= data[start]+data[end]
        if _sum==s:
            answer+=1
            break
        if _sum>s:
            break
        if _sum<s:
            answer+=1
            end+=1
            # print(start,end)
    # break

print(answer)