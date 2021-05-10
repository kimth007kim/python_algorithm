L,C=4,6
data=["a","t" ,"c", "i", "s" ,"w"]
all_out=[]
out=[]

data.sort()

def solve(depth,idx,L,C):
    if depth==L:
        all_out.append(''.join(map(str,out)))
        return
    for i in range(idx,C):
        out.append(data[i])
        solve(depth+1,i+1,L,C)
        out.pop()


solve(0,0,L,C)
print(all_out)
