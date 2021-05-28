from itertools import permutations

# n=12
# weak=[1, 5, 6, 10]
# dist=[1, 2, 3, 4]
# result=2

n=12
weak=[1, 3, 4, 9, 10]
dist=[3, 5, 7]
result=1


def solution(n, weak, dist):
    length =len(weak)
    for i in range(length):                                 # 길이를 2배로 늘여서 '원형'을 일자 형태로 변형
        weak.append(weak[i]+n)
    answer= len(dist)+1                                     # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1 로 초기화

    for start in range(length):                             # 0부터 length-1 까지의 위치를 각각 시작점으로 설정
        for friends in list(permutations(dist,len(dist))):  # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
            count=1                                         # 투입할 친구의 수
            position=weak[start]+friends[count-1]           # 해당 친구가 점검할 수 있는 마지막 위치
            print("position=",position,"weak[start]",weak[start],"friends[count-1]",friends[count-1])
            # print("start:",start,"friends:",friends,"position:",position,"weak[start]:",weak[start])
            for index in range(start,start+length):         # 시작점부터 모든 취약 지점을 확인
                print("index",index,"weak[index]",weak[index])
                if position<weak[index]:                    # 점검할수 있는 위치를 벗어나는 경우
                    print("부합!!!!!!!!!!!!! weak[index]: ", weak[index])
                    count+=1                                # 새로운 친구를 투입
                    if count > len(dist):                   # 더 투입이 불가능 하다면 종료
                        break
                    position= weak[index]+friends[count-1]
            answer=min(answer,count)                        # 최솟값 계산
    if answer > len(dist): 
        return -1            
    return answer

print(solution(n, weak, dist))