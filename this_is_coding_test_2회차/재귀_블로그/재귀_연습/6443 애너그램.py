def solution(depth,idx,st,data):
    if depth==len(data)-1:
        st+=str(data[idx])
        if st in result:
            return
        else:
            result.append(st)
    else:
        for i in range(idx,len(data)):
            solution(depth+1,idx+1,st+str(data[i]),data)
# t= int(input())
t=1
for i in range(t):
    # word=input()
    word="abc"
    wlen=len(word)
    data=[]
    result=[]
    for j in word:
        data.append(j)
    print(data)
    data.sort()
    solution(0,0,"",data)
    print(result)