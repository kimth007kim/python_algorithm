n= int(input())

arr=[]
sort_arr=[]
answer= []
def score(answer,arr,sort_arr):
    for color, size in arr:
        tmp = 0
        for d_color, d_size in sort_arr:
            if d_size>=size:
                break
            if d_color!=color and size> d_size:
                tmp+=d_size
        answer.append(tmp)

for i in range(n):
    a,b= map(int,input().split())
    arr.append([a,b])
    sort_arr.append([a,b])

sort_arr.sort(key = lambda x:x[1])
score(answer,arr,sort_arr)
for i in answer:
    print(i)

