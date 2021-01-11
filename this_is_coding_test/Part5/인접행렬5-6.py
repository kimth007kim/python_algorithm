# DFS: 깊이 우선 탐색 깊은 부분을 우선적으로 탐색하는 알고리즘

# 인접행렬: 2차원배열로 그래프의 연결관계를 표현하는 방식
# 인접 리스트: 리스트로 그래프의 연결관계를 표현하는 방식

# 인접행렬 :연결되어있지 않은 노드끼리는 무한의 비용이라고 작성 정답이 될수없는 큰값인 99999999나, 987654321등의 값으로 초기화 하는경우가 많다.
# 이렇게 그래프를 인접 행렬 방식으로 처리할때는 다음과 같이 데이터를 초기화

INF = 9999999999 #무한의 비용 선언
#2차원 리스트를 통해 인접 행렬 표현

graph=[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]]

print(graph)