x={"dog","goat","horse","tiger","fish"}
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)
print("dog"in x)
print("dog"not in x)
x.add("donkey")
print(x)
y={"red","blue","black"}
print(y)
x.update(y)
print(x)
a={"eagle","parrot","owl","peacock","pigeon"}
b={"kiwi","eagle","orange","apple","owl"}
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
f=a.symmetric_difference(b)
print(f)
a.remove("eagle")
print(a)
a.discard("blue")
print(a)
a.pop()
print(a)
a.clear()
print(a)
del a
m=frozenset({"black","red","white","yellow"})
print(m)
print(type(m))
del m 