a =int(input())
b=1
len = a
if a<=0:
    print("에러")
else:
    for i in range(a):
        star= i+1
        gong= a-star
        print(" "*gong,end="")
        print("*"*star)
        