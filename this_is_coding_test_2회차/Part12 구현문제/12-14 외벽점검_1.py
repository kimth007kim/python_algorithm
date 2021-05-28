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
    print(n,weak,dist)
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    print(weak)
    answer=len(dist)+1

    for start in range(length):
        print("!!!!!!!!!!!!!!!!!!!!start",start)
        for friends in list(permutations(dist,len(dist))):

            count=1
            position=weak[start]+friends[count-1]

            print("-----------------------------------------------")
            print("friends",friends)
            print("weak[start]",weak[start])
            print("count",count," friends[count-1]  ",friends[count-1])
            print("position=weak[start]+friends[count-1]",position)
            print("-----------------------------------------------")

            for index in range(start,start+length):
                print("index",index,"weak[index]",weak[index])
                print()
                if position<weak[index]:
                    print("점검할수있는 위치를 벗어남", position ,"<",weak[index],"count",count)
                    count+=1
                    if count > len(dist):
                        print("break문",count, len(dist))
                        break
                    position=weak[index]+friends[count-1]
                    print("계산된 값   position=weak[start]+friends[count-1]", position)
            answer=min(answer,count)
    if answer > len(dist):
        return -1
    return answer

print(solution(n, weak, dist))