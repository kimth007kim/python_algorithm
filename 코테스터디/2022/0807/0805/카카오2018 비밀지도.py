def binary(num, n):
    arr = []
    tmp = ""
    word = ""
    while num:
        word += str(num % 2)
        num = num // 2
    for i in range(len(word) - 1, -1, -1):
        tmp += word[i]

    if len(tmp) < n:
        temp = tmp
        tmp = ""
        # print("==")
        result = ""
        for i in range(n - len(temp)):
            tmp += "0"
        tmp += temp
    for i in tmp:
        arr.append(i)
    return arr


def solution(n, arr1, arr2):
    array1 = []
    array2 = []
    for i in arr1:
        array1.append(binary(i, n))
    for i in arr2:
        array2.append(binary(i, n))
    answer = []

    for i in range(n):
        tmp = ""
        for j in range(n):
            if array1[i][j] == "1" or array2[i][j] == "1":
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)
    return answer