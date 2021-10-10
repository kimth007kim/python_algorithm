def score_divide(number, arr):
    mine = arr[number]
    MAX = max(arr)
    MIN = min(arr)
    number_list = {}
    for i in arr:
        if i not in number_list:
            number_list[i] = 1
        else:
            number_list[i] += 1
    if mine == MAX or mine == MIN:
        if number_list[mine] == 1:
            del number_list[mine]
    cnt = 0
    total = 0
    for i in number_list:
        total += i * number_list[i]
        cnt += number_list[i]
    print("------", number_list, total, cnt)
    print(total / cnt)
    return total / cnt


def level_check(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 50 <= score < 70:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    dic = {}
    n = len(scores)
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(scores[i][j])
        dic[j] = tmp
    for i in dic:
        score = score_divide(i, dic[i])
        answer += level_check(score)
    return answer