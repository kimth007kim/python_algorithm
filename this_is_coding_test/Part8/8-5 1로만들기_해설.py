x =int(input())

d = [0]*100

for i in range(2,x+1):
    d[i] =d[i-1]+1                  #현재의 수에서 1을 뺴는 경우
    if i %2 ==0:                    #현재의 수가 2로 나누어 떨어지는 경우
        print("빼기,or 2나눔",d[i],d[i//2]+1)
        d[i]=min(d[i],d[i//2]+1)
        case="2나뉨"
    if i %3 ==0:
        print("빼기,or 3나눔",d[i],d[i//3]+1)
        d[i]=min(d[i],d[i//3]+1)
        case="3나뉨"
    if i %5 ==0:
        print("빼기,or 5나눔",d[i],d[i//5]+1)
        d[i]=min(d[i],d[i//5]+1)
        case="5나뉨"
    print(case,i,"=",d[i])

print(d)
print(d[x])