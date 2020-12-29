word = input()
wlist= ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in wlist:
    word= word.replace(i,'a')
print(len(word))