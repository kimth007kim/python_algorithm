numbers="17"
# numbers="011"
def dfs(cnt, d, result, answer):
    if cnt == length+1:
        for i in range(len(d)):
            answer.append(result+d[i])
        # answer.append(result)
        return
    for i in range(len(d)):
        tmp = str(d.pop(i))
        answer.append(result+str(tmp))
        # print("--------cnt------",cnt,d)
        dfs(cnt + 1, d, result + tmp, answer)
        d.append(tmp)
        d.sort()

def find(n):
    cnt=len(n)
    for i in range(len(n)):
        if n[i]==1:
            cnt-=1
            continue
        else:
            for j in range(2,n[i]):
                if n[i]%j==0:
                    cnt-=1
                    print(n[i],j)
                    break

    return cnt


def solution(numbers):
    global length
    length = len(numbers)
    answer = []
    d = []
    for i in numbers:
        d.append(i)

    tmp = ""
    for i in range(len(d)):
        dfs(0, d, tmp, answer)

    answer=list(set(answer))
    zerolist=[]
    for i in answer:
        if i[0]=="0":
            zerolist.append(i)

    for i in zerolist:
        answer.remove(i)
    n=[]
    for i in answer:
        n.append(int(i))
    n.sort()
    print(n)
    count= find(n)

    return count

print(solution(numbers))