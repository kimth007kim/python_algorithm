
#1 국어 점수가 감소하는 순서로 x[1]
#2 국어 점수가 같으면 영어 점수가 증가하는 순서로 -x[2]
#3 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 x[3]
#4 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)


n= int(input())
data=[]
# for i in range(n):
#     a,b,c,d=map(str,input().split())
#     data.append([a,b,c,d])

for _ in range(n):
    data.append(input().split())
print(data)
data.sort(key= lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
print(data)