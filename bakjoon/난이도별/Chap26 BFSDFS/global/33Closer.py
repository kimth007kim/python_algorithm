# 33.1 변수의 사용범위 알아보기
# ex1.

# x= 10
# def foo():
#     print(x)
#
# foo()
# print(x)

# ex2.

# def foo():
#     x=10
#     print(x)
#
# foo()
# print(x)

# Traceback (most recent call last):
#   File "C:/Users/Kyungdong/Documents/python_algorithm/bakjoon/난이도별/Chap26 BFSDFS/global/33Closer.py", line 13, in <module>
#     print(x)
# NameError: name 'x' is not defined

# 33.1.1  함수 안에서 전역 변수 변경하기

# ex1.
# x= 10
# def foo():
#     x=20
#     print(x)
# foo()
# print(x)

# ex2.
# x= 10
# def foo ():
#     global x
#     x=20
#     print(x)
# foo()
# print(x)

def foo():
    global x
    x=20
    print(x)
foo()
print(x)