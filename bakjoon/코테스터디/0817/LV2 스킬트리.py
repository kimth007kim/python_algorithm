def check(tree, skill):
    tmp = []
    cnt = 0
    for i in tree:
        for j in range(cnt + 1, len(skill)):
            if i == skill[j]:
                return False
        if i == skill[cnt]:
            tmp.append(i)
            cnt += 1
            if cnt == len(skill):
                return True
    return True


def solution(skill, skill_trees):
    answer = 0

    skill = list(skill)
    skill_tree = []
    for i in skill_trees:
        skill_tree.append(list(i))

    for tree in skill_tree:
        if len(tree) == 1:
            if skill[0] == tree[0]:
                answer += 1
        else:
            if check(tree, skill):
                answer += 1
    return answer