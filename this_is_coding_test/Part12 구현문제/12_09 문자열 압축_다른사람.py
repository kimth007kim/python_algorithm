source= "https://programmers.co.kr/learn/courses/30/lessons/60057"
link="https://copy-driven-dev.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-ProgrammersPython-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95"

# s="abcabcabcabcdededededede"

# output=14
# 길이:24
s="aabbaccc"
# s="abcabcdede"
# output=8
# s="xababcdcdababcdcd"
# output=17
# print("aabbaccc")


def solution(s):
    answer=len(s)
    print(len(s))
    for sl in range(1,len(s)//2+1):
        compressed=""
        prev=s[0:sl]
        print("prev",prev)
        count=1

        for i in range(sl,len(s)+sl,sl):
            print(count, s[i:i+sl])
            
            if prev== s[i:i+sl]:
                count+=1
                # print(count)
            else:
                if count != 1:
                    compressed+=str(count)+prev
                    print("1이 아닐때")
                else:
                    compressed+=prev
                    print("1일때")
                prev = s[i:i+sl]
                count=1
            print("compressed:",compressed)

        answer=min(answer,len(compressed))
    return min(answer,len(s))

print(solution(s))