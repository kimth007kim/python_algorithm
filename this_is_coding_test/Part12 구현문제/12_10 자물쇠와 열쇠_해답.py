link="https://programmers.co.kr/learn/courses/30/lessons/60059"
key= [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock= [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate90(a):
    n=len(a)
    m=len(a[0])
    result= [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] =a[i][j]
    return result

def check(new_lock):
    lock_length= len(new_lock) //3
    for i in range(lock_length,lock_length *2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j] !=1:
                return False
    return True

def solution(key, lock):
    n=len(lock)
    m=len(key)

    new_lock=[[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    # for j in new_lock:
    #     print(j)

    for rotation in range(4):
        key = rotate90(key)
        for k in new_lock:
            print(k)
        print()
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                for k in new_lock:
                    print(k)
                print()
                if check(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-= key[i][j]
    return False

print(solution(key,lock))