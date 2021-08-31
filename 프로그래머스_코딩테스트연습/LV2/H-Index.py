def solution(citations):
    citations.sort(reverse=True)
    n= len(citations)
    print(citations)
    MX=max(citations)
    for i in range(MX,-1,-1):
        high= 0
        low=0
        now=i
        for j in range(n):
            if now<=citations[j]:
                high+=1
            if now>=citations[j]:
                low+=1
        if low<=now and high>=now:
            return now
    return 0