# import sys
#
# input =sys.stdin.readline

def _graph(arr):
    graph=[ ["-" for _ in range(3)] for _ in range(3)]
    cnt=0
    X=0
    O=0
    WIN_X=False
    WIN_O=False
    blank=0
    for i in range(3):
        for j in range(3):
            if arr[cnt]=="O":
                O+=1
            elif arr[cnt]=="X":
                X+=1
            else:
                blank+=1
            graph[i][j]=arr[cnt]
            cnt+=1

    # for i in graph:
    #     print(i)

    if O>X:
        return False


    for i in range(3):
        Xx=0
        Xo=0
        Yx=0
        Yo=0
        for j in range(3):
            if graph[j][i]=="X":
                Yx+=1
            if graph[i][j]=="X":
                Xx+=1
            if graph[j][i]=="O":
                Yo+=1
            if graph[i][j]=="O":
                Xo+=1
        if Xx==3:
            WIN_X=True
        if Xo==3:
            WIN_O=True
        if Yx==3:
            WIN_X=True
        if Yo==3:
            WIN_O=True
    diagonal=[[graph[0][0],graph[1][1],graph[2][2]],[graph[2][0],graph[1][1],graph[0][2]]]
    for i in diagonal:
        # print("----------")
        tx=0
        to=0
        for j in i:
            if j =="X":
                tx+=1
            if j== "O":
                to+=1
        if tx==3:
            WIN_X=True
        if to==3:
            WIN_O=True
    if WIN_O ==True and WIN_X==True:
        return False
    if WIN_O==True and WIN_X==False and X==O:
        return True
    if WIN_X==True and WIN_O==False and X-O==1:
        return True

    if WIN_X==False and WIN_O==False and X==5 and O==4:
        return True

    return False



while True:
    tmp = input().rstrip()
    if tmp =="end":
        break
    arr = list(tmp)
    answer= _graph(arr)
    if answer:
        print("valid")
    else:
        print("invalid")