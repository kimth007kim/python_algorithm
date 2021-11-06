# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    scores = {}
    for _ in range(int(input())):
        name = input()
        number = float(input())
        if number not in scores:
            scores[number] = [name]
        else:
            scores[number].append(name)
    answer = []
    for k, v in scores.items():
        if len(v) >= 2:
            v.sort()
        answer.append([k, v])

    answer.sort(key=lambda x: x[0])
    for i in answer[1][1]:
        print(i)