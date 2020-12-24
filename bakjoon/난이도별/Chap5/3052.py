a_list = []
count = 0
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())
a0 = int(input())

a_list.append(a1 % 42)
a_list.append(a2 % 42)
a_list.append(a3 % 42)
a_list.append(a4 % 42)
a_list.append(a5 % 42)
a_list.append(a6 % 42)
a_list.append(a7 % 42)
a_list.append(a8 % 42)
a_list.append(a9 % 42)
a_list.append(a0 % 42)

my_set = set(a_list)
a_list = list(my_set)

print(len(a_list))


