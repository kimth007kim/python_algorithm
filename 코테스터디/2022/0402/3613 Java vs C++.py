import re
import sys

input = sys.stdin.readline
word= input().rstrip()
def solution(word):
    if word[0].isupper() or word[0]=="_":
        return "Error!"
    if word[len(word)-1]=="_":
        return "Error!"
    prev=""
    for i in range(len(word)):
        now = word[i]
        if prev=="_" and prev==now:
            return "Error!"
        if prev=="_" and now.isupper():
            return "Error!"

        prev =now

    if re.search("_",word):
        if re.search("[A-Z]",word):
            return "Error!"

        result=re.findall(r'_[a-z]',word)
        arr=[]
        for i in result:
            arr.append(i[1:].upper())
        for i in range(len(result)):
            word=word.replace(result[i],arr[i])
        return word

    elif re.search("[A-Z]",word):
        result=re.findall(r'[A-Z]',word)
        arr=[]
        for i in result:
            arr.append("_"+i.lower())
        for i in range(len(result)):
            word=word.replace(result[i],arr[i])
        return word

    else:
        return word

print(solution(word))