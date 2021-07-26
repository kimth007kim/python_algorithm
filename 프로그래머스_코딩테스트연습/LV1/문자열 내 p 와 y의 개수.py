def solution(s):
    plen=0
    ylen=0
    for i in s:
        if i=="P" or i =="p":
            plen+=1
        elif i=="Y" or i=="y":
            ylen+=1
    if plen==ylen:
        return True
    else:
        return False