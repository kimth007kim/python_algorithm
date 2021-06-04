N= 5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    Length=len(stages)
    cnt=1
    answer=[]
    while Length>0 and cnt<=5:
        if Length==0:
            break
        tmp=0
        for i in stages:
            if i == cnt:
                tmp+=1
        for i in range(tmp):
            stages.remove(cnt)
        answer.append((cnt,tmp/Length))
        print(answer)
        Length-=tmp
        cnt+=1
    # print(answer)
    answer=sorted(answer, key= lambda x:-x[1])
    answer=[i[0] for i in answer]
    return answer

solution(N,stages)