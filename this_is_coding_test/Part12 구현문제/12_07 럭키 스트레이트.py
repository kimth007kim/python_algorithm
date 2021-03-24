number=input()

def calculator(string):
    result=0
    for i in range(len(string)):
        result+=int(string[i])
    return result

snumber= str(number)
half = len(snumber)//2

fnum=calculator(snumber[:half])
enum=calculator(snumber[half:])

if enum==fnum:
    print("LUCKY")
else:
    print("READY")