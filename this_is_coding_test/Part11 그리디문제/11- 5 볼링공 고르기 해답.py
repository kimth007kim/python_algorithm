n,m = map(int,input().split())
data= list(map(int,input().split()))

array=[0]*11
for x in data:              # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x]+=1
print(array)

result=0    
for i in range(1,m+1):      # 1부터 m까지의 각 무게에 대하여 처리
    print(array[i])
    n-= array[i]            # 무개가 1인 볼링공의 개수(A가 선택할 수있는 개수)제외
    result += array[i] *n     # B가 선택하는 경우와 곱하기
    print("result:",result)