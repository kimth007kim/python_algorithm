import heapq

# food_times=[6, 2, 4]
# k=10

# food_times=[10, 4, 6]
# k=17
#
# food_times=[8, 6, 4]
# k=15

def solution(food_times,k):
    if sum(food_times)<=k:
        return -1

    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
        print(q)

    sum_value=0
    previous=0
    length= len(food_times)
    # print(q[0][1])

    # 현재 상황에서 음식을 다 먹어서 뺄 수 있는지 k랑 비교해야 한다.
    # sum_value와 빼버릴 음식의 시간-이전 음식 값 * 현재 음식 개수와 비교
    while sum_value+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0]
        print("now",now,"previous",previous)
        sum_value+=(now-previous)*length
        print("sum_value",sum_value)
        length -=1
        previous =now

    print(q)
    result=sorted(q,key =lambda x: x[1])
    return result[(k-sum_value)%length][1]

print(solution(food_times,k))