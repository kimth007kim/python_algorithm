import heapq

def solution(scoville, K):
    answer = 0
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    q=[]
    for i in scoville:
        heapq.heappush(q,(i))
    cnt=0
    while q:
        if len(q)<2:
            break
        else:
            r1=heapq.heappop(q)
            r2=heapq.heappop(q)
            recipe= r1+(r2*2)
            heapq.heappush(q,(recipe))
            cnt+=1
            length=len(q)
            check=0
            if q[0]>=K:
            # for i in q:
            #     if K<= i:
            #         check+=1
            # if length==check:
                return cnt
    return -1