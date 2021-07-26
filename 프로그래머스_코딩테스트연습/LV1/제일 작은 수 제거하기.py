def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        MIN = int(1e9)
        for i in arr:
            if i < MIN:
                MIN = i
        arr.remove(MIN)
        return arr
