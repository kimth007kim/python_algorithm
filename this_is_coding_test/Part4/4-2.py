data= input()
x= int(ord(data[0]))-int(ord('a'))+1
y=int(data[1])
cnt=0

if x+2<=8:
    if y+1<=8 and y-1>=1:
        cnt+=2
    elif y+1<=8:
        cnt+=1
    elif y-1>=1:
        cnt+=1
if y+2<=8:
    if x + 1 <=8 and x - 1 >= 1:
        cnt += 2
    elif x +1<=8:
        cnt += 1
    elif x-1>=1:
        cnt += 1
if x-2>=1:
    if y + 1 <= 8 and y - 1 >= 1:
        cnt += 2
    elif y + 1 <= 8:
        cnt += 1
    elif y - 1 >= 1:
        cnt += 1
if y-2>=1:
    if x + 1 <=8 and x - 1 >= 1:
        cnt += 2
    elif x +1<=8:
        cnt += 1
    elif x-1>=1:
        cnt += 1

print(cnt)