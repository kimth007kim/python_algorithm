n=int(input())
ugly=[0]*n
ugly[0]=1

i2=i3=i5=0
next2,next3,next5=2,3,5

for l in range(1,n):
    ugly[l]=min(next2,next3,next5)
    print("현재-----",l)
    if ugly[l]==next2:
        i2+=1
        next2=ugly[i2]*2
        print("next2",next2)
    if ugly[l]==next3:
        i3+=1
        next3=ugly[i3]*3
        print("next3",next3)
    if ugly[l]==next5:
        i5+=1
        next5=ugly[i5]*5
        print("next5",next5)
    print(l," = ", ugly[l])
    print("next2,next3,next5",next2,next3,next5)

print(ugly)