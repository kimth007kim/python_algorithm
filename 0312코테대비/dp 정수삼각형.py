n=int(input())
triangle=[]

for _ in range(n):
    triangle.append(list(map(int,input().split())))
def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                up_left = 0
            else:
                up_left = triangle[i - 1][j - 1]
            if j == i:
                up = 0
            else:
                up = triangle[i - 1][j]

            triangle[i][j] = triangle[i][j] + max(up_left, up)
            print(i,j,triangle[i][j],triangle)
    answer = max(triangle[len(triangle) - 1])
    return answer

print(solution(triangle))