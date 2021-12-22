from itertools import permutations


def finder(word, idx, op):
    end = idx + 1
    start = idx - 1
    for i in range(idx + 1, len(word)):
        if word[i] == "*" or word[i] == "-" or word[i] == "+":
            break
        end = i

    for i in range(idx - 1, -1, -1):
        if word[i] == "*" or word[i] == "-" or word[i] == "+":
            break
        start = i
    temp = word[start:end + 1].replace("*", " ", ).replace("-", " ").replace("+", " ")
    if " " not in temp:
        return word

    n1, n2 = map(int, temp.split())
    if op == "*":
        result = n1 * n2
    elif op == "-":
        result = n1 - n2
    else:
        result = n1 + n2
    print("     시작   " + word[:start] + "      답:  " + str(result) + "     끝   " + word[end + 1:])
    word = word[:start] + str(result) + word[end + 1:]
    print(word)
    return word


def calc(arr, word, dic):
    for op in arr:
        for i in range(dic[op]):
            for k, v in enumerate(word):
                if v == op:
                    print("_____________________________________")
                    word = finder(word, k, op)
                    print("_____________________________________")
                    break


def solution(expression):
    arr = []
    dic = {}
    for i in expression:
        if i == "*" or i == "+" or i == "-":
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
    for i in dic:
        arr.append(i)
    perm = list(permutations(arr, len(arr)))

    for i in perm:
        calc(i, expression[:], dic)
    answer = 0
    return answer

print(solution("100-200*300-500+20"))