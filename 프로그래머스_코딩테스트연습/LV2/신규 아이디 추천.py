def solution(new_id):
    # 1단계 대문자를 전부 소문자로 치환
    # LENGTH=len(new_id)
    word = []
    for i in new_id:
        word.append(i)
    for i in range(len(word)):
        chract = ord(word[i])
        if 65 <= chract <= 90:
            word[i] = chr(chract + 32)

    # 2단계 모든 특수문자제거
    DelList = []
    for i in range(len(word)):
        if 97 <= ord(word[i]) <= 122:
            continue
        if 45 <= ord(word[i]) <= 46:
            continue
        if 48 <= ord(word[i]) <= 57:
            continue
        if ord(word[i]) == 95:
            continue
        DelList.append(word[i])
    for i in DelList:
        word.remove(i)

    # 3단계 .이 2개이상이면 한개 제거
    # print("3단계 시작전",word)
    tmp3 = []
    cnt = 0
    point = 0
    for i in range(len(word)):
        # if word[i]=="." and i!=len(word)-1:
        #     cnt+=1
        # if cnt>=2:
        #     tmp3.append(i)
        if word[i] == "." and word[i - 1] == "." and i >= 1:
            tmp3.append(i)

        # if (cnt>=2) or (cnt>=1 and word[i]=="." and i==len(word)-1):
        #     cnt=0
        #     tmp3.append(i)
    # print(tmp3)
    cnt = 0
    # print(word)
    # print(tmp3)
    for i in tmp3:
        word.pop(i + cnt)
        # print(word)
        cnt -= 1
        # print("3단계 후반",word)
    # print(word)

    # 4번 처음이나 마지막 . 이면 제거
    # print("4단계초반",word)
    if len(word) >= 1:
        if word[0] == ".":
            word.pop(0)
    if len(word) >= 1:
        if word[len(word) - 1] == ".":
            word.pop(len(word) - 1)
    # print("4단계 후반",word)
    # print(word)

    # 5단계 빈문자열이면 a대입
    if len(word) == 0:
        word.append("a")
    # print(word)

    # 6단계 16자이상이면 15개문자 제외하고 모두제거
    if len(word) >= 16:
        word = word[:15]
        # print(word)
        if word[len(word) - 1] == ".":
            word.pop(len(word) - 1)
    # print(word)

    # 7단계 new_id의 길이가 2글자 이하라면 마지막글자 반복
    if len(word) <= 2:
        # print(word)
        tmcase = word[len(word) - 1]
        while len(word) < 3:
            word.append(tmcase)
        # print(word)

    return "".join(word)