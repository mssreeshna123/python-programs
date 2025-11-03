# num=int(input("enter a number"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not a prime number")
#             break
#     else:
#             print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")            

# def count_vowels(text):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in text:
#         if char in vowels:
#             count+=1
#     return count
# string=input("enter a string")
# print("number of vowels is",count_vowels(string))

# num1=int(input("enter first number"))
# operator=input("enter operator(+,-,*,/)")
# num2=int(input("enter second number"))
# if operator=="+":
#     print(num1+num2)
# elif operator=="-":
#     print(num1-num2)
# elif operator=="*":
#     print(num1*num2)
# elif operator=="/":
#     if num2!=0:
#         print(num1/num2)
#     else:
#         print("division by zero is not allowed")
# else:
#     print("invalid opertor")

# string=input("enter a string")
# start=0
# end=len(string)-1
# is_palindrome=True
# while start<end:
#     if string[start]!=string[end]:
#         is_palindrome=False
#         break
#     start+=1
#     end-=1
# if is_palindrome:
#     print("the string is palindrome")
# else:
#     print("the string is not palindrome")

x=["red","black","green","white","yellow"]
print(x)
print(type(x))
print(len(x))
print(x[2])
print(x[3:5])
print(x[1:])
print(x[:3])
print(x[-3])
print(x[-4:-2])
print(x[-4:])
print(x[:-3])
print("red"in x)
print("red"not in x)
for i in x:
    print(i)
x[3]="blue"
print(x)
x.append("orange")
print(x)
x.insert(2,"golden")
print(x)
y=[1,2,3,4,5]
x.sort()
print(x)
x.sort(reverse=True)
print(x)
x.extend(y)
print(x)
z=x.copy()
print(z)
print(x.count("red"))
a=list(x)
print(a)
del x[4]
print(x)
x.pop()
print(x)
x.pop(5)
print(x)
x.clear()
print(x)
del x

x=("apple","orange","grape","lemon","kiwi")
print(x)
print(type(x))
print(len(x))



