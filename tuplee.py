x=["one","two","three","four","five"]
print(x)
print(type(x))
print(len(x))
print(x[3])
print(x[2:5])
print(x[2:])
print(x[:4])
print(x[-1])
print(x[-2:])
print(x[-5:-2])
print(x[:-4])
print("one"in x)
print("one"not in x)
for i in x:
    print(i)
x[1]="ten"
print(x)
x.append("eight")
print(x)
x.insert(2,"nine")
print(x)
y=["red","blue","green"]
x.extend(y)
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
x.pop(2)
print(x)
x.pop()
print(x)
del x[4] 
print(x)
print(x.count("one"))
x.remove("three")
print(x)
x.copy()
print(x)
z=list(x)


a=("cat","cow","hen","dog","elephant")
print(a)
print(type(a))
print(len(a))
print(a[1])
print(a[3:5])
print(a[:3])
print(a[2:])
print(a[-3])
print(a[-4:-1])
print(a[:-2])
print(a[-3:])
print("dog"in a)
print("dog"not in a)
for i in a:
    print(i)
b=list(a)
print(b)
print(type(b))
b.insert(1,"rat")
print(b)
b[5]="snake"
print(b)
b.pop(2)
print(b)
a=tuple(b)
print(a)
c=("blue","black","yellow")
print(a+c)
d=c*2
print(d)
print(d.count("blue"))









