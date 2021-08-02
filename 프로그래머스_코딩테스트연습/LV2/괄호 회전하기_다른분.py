from collections import deque


def check(string):
    stack = []
    for s in string:
        if len(stack) == 0:
            if s == ')' or s == '}' or s == ']':
                return False
        if s == '(' or s == '{' or s == '[':
            stack.append(s)
        else:
            if s == ')' and stack[-1] == '(':
                stack.pop()
            if s == '}' and stack[-1] == '{':
                stack.pop()
            if s == ']' and stack[-1] == '[':
                stack.pop()
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    q = deque(list(s))
    i = 0
    while i != len(q):
        if check(q):
            answer += 1
        q.rotate(-1)            # q를 요소들을 매개 변수만큼 회전 매개변수가 음수이면 왼쪽으로 회전, 양수이면 오른쪽으로 회전
        print(q)
        i += 1

    return answer