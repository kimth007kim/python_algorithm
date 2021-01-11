#재귀함수가 언제 끝날지 종료 조건을 꼭 명시해야한다.자칫 명시하지않으면 무한호출
# 초반의 if문이 종료 조건 역할 수행

def recursive_function(i):
    #100번쨰 출력했을때 종료되도록 종료 조건 명시
    if i == 3:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')

recursive_function(1)