# 진법 초기화
a = 10
print(type(a), a)
a = 0b10
print(type(a), a)
a = 0o10
print(type(a), a)
a = 0x10
print(type(a), a)
print()
a = 0B10
print(type(a), a)
a = 0O10
print(type(a), a)
a = 0X10
print(type(a), a)
print("-"*20)

# 출력
i = 0x100
print("i = ", i)
print("i = ", bin(i))
print("i = ", int(i))
print("i = ", oct(i))
print("i = ", hex(i))
print("-"*20)

# 문자열을 형변환
i = "111"
print("i = ", int(i))
print("i = ", int(i, 2))
print("i = ", int(i, 8))
print("i = ", int(i, 16))
print("i = ", int(i, 5))
print("-"*20)