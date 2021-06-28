def solution(answers):
    people = ['12345', '21232425', '3311224455']
    dab = []
    word = ''
    for i in answers:
        word += str(i)
    result = []

    for i in range(len(people)):
        print(people[i])
        match = check(word, people[i])
        result.append((match, i + 1))
    print(result)
    Mnumber = 0
    for a, b in result:
        if a > Mnumber:
            Mnumber = a

    for match, n in result:
        if match == Mnumber:
            dab.append(n)
    return dab


def check(word, p):
    LENGTH = len(word)
    tmp = p
    while LENGTH != len(p):
        if LENGTH < len(p):
            p = p[:LENGTH]
        if LENGTH > len(p):
            p += tmp
    match = 0
    for i in range(len(word)):
        if word[i] == p[i]:
            match += 1
    return match