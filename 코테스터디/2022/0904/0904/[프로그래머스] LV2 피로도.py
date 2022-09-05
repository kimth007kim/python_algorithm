from itertools import permutations

def solution(k, dungeons):
    MAX=0
    length= len(dungeons)
    comb=permutations(dungeons,length)
    for i in comb:
        total= k
        cnt=0
        for req,cost in i:
            if req>total:
                break
            total-=cost
            cnt+=1
        # print(cnt)
        MAX=max(MAX,cnt)
    answer = -1
    return MAX