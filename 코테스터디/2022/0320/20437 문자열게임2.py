# 작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.
#
# 1. 알파벳 소문자로 이루어진 문자열 W가 주어진다.
# 2. 양의 정수 K가 주어진다.
# 3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 4. 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
# 위와 같은 방식으로 게임을 T회 진행한다.
import sys
input = sys.stdin.readline


def game(word,n):
    result = []
    dic={}
    for i,j in enumerate(word):
        if j not in dic:
            dic[j]=[]
            dic[j].append(i)
        else:
            dic[j].append(i)

    for i in dic:
        if len(dic[i])<n:
            continue
        for j in range(len(dic[i])-n+1):
            tmp=dic[i][j:j+n]
            LENGTH= tmp[-1]-tmp[0]+1
            result.append(LENGTH)

    if len(result)==0:
        return -1
    else:
        result.sort()
        MIN=result[0]
        MAX=result[-1]
        return str(MIN)+" "+str(MAX)
answer=[]
for i in range(int(input())):
    word =input()
    n= int(input())
    answer.append(game(word, n))

for i in answer:
    print(i)
