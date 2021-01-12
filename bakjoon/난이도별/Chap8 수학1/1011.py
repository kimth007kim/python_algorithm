# T = int(input())
#
# for i in range(T):
#     x,y= map(int,input().split())

x,y=0,3
# x,y=1,5
# x,y=10,21
# x,y=45,50
speed=1
cnt=0
boost= y-x-2
cnt+=2
# print("boost=",boost)
while boost!=0:

    if boost-speed+1>=1:
        speed+=1
    elif boost>2:
        speed-=1
    # print('speed',speed)
    # print("boost",boost)
    boost-=speed
    cnt+=1

else:
    print("2")

# 10  21
# 11-2=9
#  2 3 2 1