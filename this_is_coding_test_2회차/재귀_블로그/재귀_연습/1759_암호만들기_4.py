L,C=4,6
alpha=["a","t" ,"c", "i", "s" ,"w"]
all_out=[]
out=[]

alpha.sort()

def solve(depth,idx,L,C):
    if depth==L:
        all_out.append(''.join(map(str,out)))
        return
    for i in range(idx,C):
        out.append(alpha[i])
        solve(depth+1,i+1,L,C)
        out.pop()

def password(list_check):
    for i in list_check:
        mo=0
        ja=0
        for j in i:
            if j in 'aeiou':
                mo+=1
            else:
                ja+=1
        if mo>=1 and ja>=2:
            print(i)
    return

solve(0,0,L,C)
password(all_out)

