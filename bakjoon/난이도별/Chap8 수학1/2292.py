# 1 =1   1 개
# 2~7 = 2 6개
# 8~ 19 =3 12개
# 20~37 =4
num=6
cross=1
cnt=1
a = int(input())
if a ==1:
    print(1)
else:
    while True:
        cross+=num
        print(cross)
        cnt+=1
        if a <= cross:
            print(cnt)
            break
        num+=6