# try:
#     print(x)
# except:
#     print("there is an error")

# try:
#     print("x")
# except NameError:
#     print("check the variable")
# except:
#     print("there is an error")
# else:
#     print("there is no error")
# finally:
#     print("completed")

# x=int(input("enter a postive number"))
# if x<0:
#     raise Exception("negative numbers are not allowed")
# else:
#     print(x)


def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cannot divide by zero"
x=int(input("enter first number"))
y=int(input("enter second number"))
print(division(x,y))


