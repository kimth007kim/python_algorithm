# DFS와 BFS를 구현하려면 재귀함수도 이해해야한다.
# 재귀함수: 자기자신을 호출하는 함수
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 에러발생 재귀의 최대 깊이를 초과했기때문에 에러 발생