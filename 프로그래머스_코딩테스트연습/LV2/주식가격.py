def solution(prices):
    LENGTH = len(prices)
    data = [0] * LENGTH
    for i in range(LENGTH):
        cnt = 1
        for j in range(i + 1, LENGTH):
            # print(i,j,cnt)
            if j == LENGTH - 1:
                data[i] = cnt
            if i == j + 1:
                if prices[i] > prices[j]:
                    data[i] = 1
                    break
            else:
                if prices[i] > prices[j]:
                    data[i] = cnt
                    break
                else:
                    cnt += 1

    return data