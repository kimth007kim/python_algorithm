def solution(s):
    answer = ""
    dict = {}
    dict["zero"] = "0"
    dict["one"] = "1"
    dict["two"] = "2"
    dict["three"] = "3"
    dict["four"] = "4"
    dict["five"] = "5"
    dict["six"] = "6"
    dict["seven"] = "7"
    dict["eight"] = "8"
    dict["nine"] = "9"
    prev = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            prev += i
            if prev in dict:
                answer += dict[prev]
                prev = ""

    # print(answer)

    return int(answer)