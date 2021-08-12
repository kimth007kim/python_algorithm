data = input()
n = int(input())

cursor=len(data)
print(cursor,data)
for i in range(n):
    command = input()
    if "P" in command:
        put, ch= map(str,command.split())
        data.insert(cursor+1,ch)
    elif command=="L":
        if cursor!=0:
            cursor-=1
    elif command == "D":
        if cursor != len(data)+1:
            cursor += 1
    elif command == "B":
        if cursor !=0:
            if cursor==len(data):
                data.pop(cursor-1)
                cursor-=1
            else:
                data.pop(cursor-1)