from itertools import permutations

def check(users, banned_id):
    print(users, banned_id)
    for i in range(len(users)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            elif banned_id[i][j] == users[i][j]:
                continue
            else:
                print("      불합       ", users, users[i], banned_id[i])
                return False

    print("      합격        ", users, users[i], banned_id[i])
    return True


def solution(user_id, banned_id):
    USER = list(permutations(user_id, len(banned_id)))
    banned_Set = []
    data = []
    for users in USER:
        if not check(users, banned_id):
            continue
        users = set(users)
        # print(users)
        if users not in banned_Set:
            banned_Set.append(users)
            # print(users)
    print(banned_Set)
    answer = 0
    return answer