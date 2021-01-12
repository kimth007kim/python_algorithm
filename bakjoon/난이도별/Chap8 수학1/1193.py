# 5시 11분 시작 5시36분완료

# 1/1
#
# 1/2 2/1
#
# 3/1 2/2 1/3
#
# 1/4 2/3 3/2 4/1
#  7   8   9   10
# 5/1 4/2 3/3 2/4 1/5
#              14  15
X = int(input())

line = 1

while X > line:
    X-=line
    line+=1

if line %2 ==0:
    a= X
    b= line -X+1
else:
    a=line -X+1
    b=X

print(a,"/",b,sep="")