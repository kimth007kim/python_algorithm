import sys

input = sys.stdin.readline


def dfs(now, cnt, sign):
    global MAX, MIN
    if cnt == n:
        # print(now, " ", cnt, sign)
        MIN = min(MIN,now)
        MAX = max(MAX,now)
        return
    for i in range(4):
        if sign[i] <= 0:
            continue
        sign[i] -= 1
        tmp = now
        if i == 0:
            tmp += arr[cnt]
        elif i == 1:
            tmp -= arr[cnt]
        elif i == 2:
            tmp *= arr[cnt]
        elif i == 3:
            tmp = int(tmp/arr[cnt])
            # tmp //= arr[cnt]

        dfs(tmp, cnt + 1, sign)
        sign[i] += 1


n = int(input())
arr = list(map(int, input().split()))
sign = list(map(int, input().split()))
MAX = -int(1e15)
MIN = int(1e15)

# for i in range(4):
dfs(arr[0], 1, sign)

print(MAX)
print(MIN)
