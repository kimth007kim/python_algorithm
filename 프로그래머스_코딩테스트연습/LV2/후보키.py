from itertools import combinations

relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]


def checkCandidate(colLst, rows):
    tmp = [tuple([item[idx] for idx in colLst]) for item in relation]
    # print(tmp)
    if len(set(tmp)) != rows:
        return False
    else:
        return True

def solution(relation):


    rows = len(relation)
    cols = len(relation[0])
    colLst = range(cols)

    lst = []
    for leng in range(1, cols + 1):
        comb = combinations(colLst, leng)
        for n1 in list(comb):
            # print(n1)
            if checkCandidate(n1, rows):
                lst.append(set(n1))


    for el1 in lst[:]:
        for el2 in lst[:]:
            print("el1, el2",el1 ,"   ",el2)
            if el1 == (el1 & el2):
                if el1 != el2:
                    lst.remove(el2)

    print(lst)
    return len(lst)

print(solution(relation))