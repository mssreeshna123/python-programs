# def print_name():
#     print("my name is sreeshna")
# print_name()
# print_name()


# def addition():  
#     print(x+y)
# x=int(input("enter first number"))
# y=int(input("enter second number"))
# addition()
# print(x)

# def add(x,y):
#     print(x+y)
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# add(a,b)

# def substract(x,y):
#     print(x-y)
#     print(x*y)
#     print(x/y)
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# substract(a,b)

# def arbitrary(*x):
#     print(x[1]+x[3])
# arbitrary(2,4,6,8,3,5)

# def keyword(x,y,z):
#     print(x-y)
# keyword(z=5,x=8,y=6)

# def arbitrary_keyword(**x):
#     print(x["a"]+x["c"])
# arbitrary_keyword(b=3,a=6,d=7,c=4,e=2)

# def defparam(x=100):
#     print(x)
# defparam(90)
# defparam()

# def retstmnt(x,y):
#     return x+y
# print(retstmnt(8,6))

# print(100+retstmnt(6,4))

# def evenodd(x):
#     if x%2==0:
#         print("the number is even")
#     else:
#         print("the number is odd")
# a=int(input("enter no:"))
# evenodd(a)

# def even(x,y):
#     for i in range(x,y+1):
#         if i%2==0:
#             print(i)
# a=int(input("enter start:"))
# b=int(input("enter the limit:"))
# even(a,b)

# def fact(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         return x*fact(x-1)
# print(fact(5))

# def natural_number(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum
# natural_number(10)
# print("sum of first 10 natural number is",natural_number(10))

# def even_number(x,y):
#     sum=0
#     for i in range(x,y+1):
#         if i%2==0:
#             sum+=i
#     return sum
# x=int(input("enter starting number"))
# y=int(input("enter ending number"))
# print("sum of even numbers is",even_number(x,y))

# def prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print(n,"is not a prime number")
#                 break
#         else:
#             print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")
# n=int(input("enter a number"))
# prime(n)
