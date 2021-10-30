from itertools import combinations


def find_max(arr,number):
    tmp=""
    for j in arr:
        tmp+=number[j]
    # return int(tmp)
    return tmp

def solution(number, k):
    length= len(number)
    MAXIMUM=-1
    p = list(combinations(range(length),length-k))
    answer= []
    for i in p:
        t= find_max(i,number)
        answer.append(t)
    answer.sort(reverse= True)
    return str(answer[0])