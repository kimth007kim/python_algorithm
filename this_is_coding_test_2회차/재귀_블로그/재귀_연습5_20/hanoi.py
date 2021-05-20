n=3

def hanoi(n,start,end):
    if n==1:
        print(n,start,end)
        return
    hanoi(n-1,start,6-start-end)
    print(n,start,end)
    hanoi(n-1,6-start-end,end)


hanoi(n,1,3)

