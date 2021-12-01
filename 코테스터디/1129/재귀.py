answer=0

def MOVE(i):
    if i ==0:
        return 0
    if i ==1 :
        return 1
    if i ==2:
        return 2
    if i ==3:
        return 3

def recur(cnt,answer,arr):
    if cnt==0:
        return

    print(cnt, answer,arr)

    for i in range(4):
        arr.append(MOVE(i))
        recur(cnt-1,answer+MOVE(i),arr)
        arr.remove(MOVE(i))



recur(4,answer,[])