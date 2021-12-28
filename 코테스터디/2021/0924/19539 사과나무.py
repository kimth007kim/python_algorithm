

# 이하는 최근 사과나무 씨앗을 구매하여 농장 뒷뜰에  일렬로 1번부터 N 번까지 심었다. 이 나무들의 초기 높이는 모두 0
 # n=3  0 0 0


n= int(input())
data= list(map(int,input().split()))
# n=2
# data= [4, 3]
# print(n,data)

if sum(data)%3!=0:
    print("NO")
else:
    cnt=0
    for i in range(len(data)):
        if data[i] %3 ==0:
            data[i]==0
            continue
        else:
            cnt+=data[i]//2
            data[i]= data[i]%2
        # data[i]=1
    print(data)
    print(cnt)