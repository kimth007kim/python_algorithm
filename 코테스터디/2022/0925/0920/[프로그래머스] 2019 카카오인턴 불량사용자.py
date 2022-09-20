from itertools import combinations, permutations


def check(user, ban):
    if len(user) != len(ban):
        return False
    for i in range(len(user)):
        if ban[i] == "*":
            continue
        if ban[i] != user[i]:
            return False
    return True


def match(user, ban):
    global answer

    for bid in ban:
        cnt = 0
        for j in range(len(user)):
            if check(user[j], bid[j]) == True:
                cnt += 1

        if cnt == len(user):
            answer += 1
            return


def solution(user_id, banned_id):
    global answer
    answer = 0

    comb = list(combinations(user_id, len(banned_id)))
    ban = list(permutations(banned_id, len(banned_id)))
    for u in comb:
        match(u, ban)

    return answer