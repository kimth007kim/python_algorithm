from collections import deque

n, m = map(int, input().split())
INF = int(1e9)
dp = [INF] * 100001
count = [0] * 100001
q = deque()
q.append([n, 0])
count[n]=1
dp[n] = 0
while q:
    now, cnt = q.popleft()
    if now == m:
        continue
    # print(now,cnt,count)
    if now*2 < len(dp):
        if dp[now * 2] == cnt + 1:
            count[now * 2] += 1
            q.append([now*2,cnt+1])

        if dp[now * 2] > cnt + 1:
            dp[now * 2] = cnt + 1
            q.append([now * 2, cnt + 1])
            count[now * 2] = 1

    if now + 1 < len(dp):
        if dp[now + 1] == cnt + 1:
            count[now + 1] += 1
            q.append([now +1, cnt + 1])

        if dp[now + 1] > cnt + 1:
            dp[now + 1] = cnt + 1
            q.append([now + 1, cnt + 1])
            count[now + 1] = 1
    if now - 1 >= 0:
        if dp[now - 1] == cnt + 1:
            count[now - 1] += 1
            q.append([now - 1, cnt + 1])
        if dp[now - 1] > cnt + 1:
            dp[now - 1] = cnt + 1
            q.append([now - 1, cnt + 1])
            count[now - 1] = 1
print(dp[m])
print(count[m])