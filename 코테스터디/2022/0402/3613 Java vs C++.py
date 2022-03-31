import re
import sys

input = sys.stdin.readline
word= input().rstrip()
def solution(word):

    if re.search("_",word):
        print("1단계")
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
        if word[0].isupper():
            return "Error!"
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