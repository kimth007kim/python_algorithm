def sum_all(arr):
    ret =0              #1
    for elem in arr:    #2
        ret += elem     #3
    return ret
arr=[1,2,3]
print(sum_all(arr))