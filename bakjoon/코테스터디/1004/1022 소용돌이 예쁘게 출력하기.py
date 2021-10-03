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
    for i in range(length):
        px += dx[direction]
        py += dy[direction]
        data[px][py] = number
        number -= 1

    direction = (direction + 1) % 4

    return px,py,direction,number



tmp = list(map(int,input().split()))
maximum= lengthFinder(tmp)

for i in range(4):
    tmp[i]+=maximum
length = 1+(2*maximum)
data = [[0]*length for i in range(length)]


number = length*length
for i in range(length):
    data[length-1][length-1-i]=number
    number-=1

px = length-1
py= 0
direction+=1
length-=1


cnt=0
while number!=0:
# for i in range(4):
    px,py,direction,number=snailArray(px,py,direction,number)
    cnt+=1
    if cnt %2 ==0:
        length-=1

r1,c1,r2,c2= tmp

array = [[0]*(c2+1-c1) for _ in range(r2+1-r1)]
MAX_len=0
for i in range(r1,r2+1):
    for j in range(c1,c2+1):
        array[i-r1][j-c1]= data[i][j]
        MAX_len=max(MAX_len,len(str(data[i][j])))

x_len= r2+1-r1
y_len =c2+1-c1
for i in range(x_len):
    word=""
    for j in range(y_len):
        if j!=0:
            word+=" "
        if len(str(array[i][j]))<MAX_len:
            for _ in range(MAX_len-len(str(array[i][j]))):
                word+=" "
        word+=str(array[i][j])
    print(word)
