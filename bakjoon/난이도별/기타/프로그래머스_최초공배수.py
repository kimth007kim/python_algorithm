a= [1,2,3]
b=[2,4,6,14]
c=[2,4,8,16]

def Quiz(arr):
    answer=0
    minNUM=MIN(arr)
    d=[]
    for i in arr:
        d.append(i//minNUM)
    print(d)
    result=minNUM
    for j in d:
        result *=j
    return result


def MIN(arr):
    mn= min(arr)
    cnt=0
    for i in range(max(arr),min(arr)-1,-1):
        cnt=len(arr)
        for j in arr:
            if j % i !=0:
                continue
            if j%i ==0:
                cnt-=1
        if cnt ==0:
            return i
print(Quiz(c))