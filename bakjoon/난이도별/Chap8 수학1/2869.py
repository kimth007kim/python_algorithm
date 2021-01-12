# 5시 36분 시작 5시 52분 끝

A,B,V = map(int,input().split())
c= (V-A) % (A-B)
if c ==0:
    print((V-A)//(A-B)+1)
else:
    print((V - A) // (A - B)+2)