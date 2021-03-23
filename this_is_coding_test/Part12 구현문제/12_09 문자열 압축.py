source= "https://programmers.co.kr/learn/courses/30/lessons/60057"

s="abcabcabcabcdededededede"
# output=14
# 길이:24

# s="abcabcdede"
# output=8
# s="xababcdcdababcdcd"
# output=17

def solution(s):
    answer=len(s)
    for step in range(1,len(s)//2+1):
        compressed=""
        prev=s[0:step]
        count=1

        for j in range(step,len(s),step):
            if prev== s[j:j+step]:
                count+=1
            else:
                compressed+= str(count)+prev if count>=2 else prev
                prev = s[j:j+step]
                count=1
                # print(compressed)
        compressed+=str(count)+prev if count>= 2 else prev

        answer= min(answer,len(compressed))
    return answer


print(solution(s))