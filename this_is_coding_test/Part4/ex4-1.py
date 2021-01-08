a= int(input())
x=1
y=1
data = list(map(str,input().split()))

for i in range(len(data)):
    if data[i]=="R":
        if x < a:
            x+=1
    elif data[i] == "L":
        if x > 1:
            x -=1
    elif data[i] == "U":
        if y > 1:
            y -=1
    elif data[i] == "D":
        if y < a:
            y +=1
print(y,x)