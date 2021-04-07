n= int(input())
num= list(map(int,input().split()))
case=list(map(int,input().split()))
cnt=0
answer=[]
for i in range(len(case)):
    cnt+=case[i]

result=0

def dfs(num,cnt,result,case):
    print(cnt)
    if cnt==0:
        answer.append(result)

    if cnt == n-1:
        k= num.pop(0)
        result+=k

    else:
        for i in range(4):
            NUMBER=num.pop(0)
            if case[0]>0:
                temp=case[0]
                case[0]=temp-1
                result+=NUMBER
                cnt-=1
                dfs(num, cnt, result, case)
            elif case[1]>0:
                temp = case[0]
                case[0] = temp - 1
                result -= NUMBER
                cnt -= 1
                dfs(num, cnt, result, case)
            elif case[2]>0:
                temp = case[0]
                case[0] = temp - 1
                result *= NUMBER
                cnt -= 1
                dfs(num, cnt, result, case)
            elif case[3]>0:
                temp = case[0]
                case[0] = temp - 1
                result -= NUMBER
                cnt /= 1
                dfs(num, cnt, result, case)



dfs(num, cnt, result, case)

print(answer)