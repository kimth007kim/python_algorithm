a = int(input())

for i in range(a):
    if i==0:
        print("*")
    elif i>0:
        print("*"*(i+1))
    else:
        print("에러")