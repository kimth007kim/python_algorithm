
INF=int(1e9)


dx= [0,-1,0,1]
dy= [-1,0,1,0]

direction=0




def lengthFinder(arr):
    MAX=-INF
    for i in arr:
        MAX= max(MAX,abs(i))

    return MAX

def snailArray(px,py,direction,number):
    global MAX_len
    for i in range(length):
        px += dx[direction]
        py += dy[direction]
        if r1 <= px <= r2 and c1 <= py <= c2:
            MAX_len = max(MAX_len, number)
            array[px - r1][py - c1] = number
        number -= 1

    direction = (direction + 1) % 4

    return px,py,direction,number



tmp = list(map(int,input().split()))
maximum= lengthFinder(tmp)

for i in range(4):
    tmp[i]+=maximum

r1,c1,r2,c2= tmp

length = 1+(2*maximum)
array = [[0]*(c2+1-c1) for _ in range(r2+1-r1)]



MAX_len=0
number = length*length

px= length-1
py= length-1

for i in range(length):
    if i != 0:
        px += dx[direction]
        py += dy[direction]
    if r1<= px<=r2 and c1<=py<=c2:
        array[px-r1][py-c1]=number
        MAX_len= max(MAX_len,number)





    number-=1


direction+=1
length-=1
cnt=0


# for k in range(4):
while number!=0:
    px,py,direction,number=snailArray(px,py,direction,number)
    cnt+=1
    if cnt %2 ==0:
        length-=1

x_len= r2+1-r1
y_len =c2+1-c1



MX=len(str(MAX_len))

for i in range(x_len):
    word=""
    for j in range(y_len):
        if j!=0:
            word+=" "
        if len(str(array[i][j]))<MX:
            for _ in range(MX-len(str(array[i][j]))):
                word+=" "
        word+=str(array[i][j])
    print(word)