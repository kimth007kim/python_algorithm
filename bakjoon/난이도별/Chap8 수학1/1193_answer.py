X = int(input())

line=1
while X>line:
    X-=line
    line+=1
    print("X=",X)
    print("l",line)

#
# if line %2 ==0:
#     print("line%2==0")
#     a =X
#     b=line-X+1
#     print(a,'/',b,sep='')
# else:
#     print("line%2!=0")
#     a=line-X+1
#     b=X
#     print(a,'/',b,sep='')
# print(a,'/',b,sep='')
