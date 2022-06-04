n,m = map(int,input().split())
tmp=list(map(int,input().split()))
height_dict={}

arr=[]
for i in range(n):
    height_dict[i+1]=tmp[i]
    arr.append([tmp[i],i+1])

arr.append([0,0])
arr.sort(reverse=True)
graph=[[] for _ in range(n+1)]
amount=[0]*(n+1)
print(height_dict)
for i in range(m):
    a,b= map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

print(graph)
for i in range(n):
    height,num= arr[i][0],arr[i][1]
    MAX=0
    for j in graph[num]:
        # if height_dict[j]<height:
        #     print(num,j)
        MAX=max(MAX,amount[j])
    amount[num]=MAX+1
    print(amount)

print(amount)