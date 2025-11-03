x={"cat","cow","dog","monkey","donkey"}
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)
print("cat"in x)
print("cat"not in x)
x.add("snake")
print(x)
y={"blue","yellow","white"}
print(y)
x.update(y)
print(x)
a={"rose","jasmine","sunflower","lilly","lotus"}
b={"red","rose","blue","lotus","black"}
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
f=a.symmetric_difference(b)
print(f)
a.remove("rose")
print(a)
a.discard("blue")
print(a)
a.pop()
print(a)
a.clear()
print(a)
del x
m=frozenset({"apple","orange","watermelon","lemon","grape"})
print(m)
print(type(m))
a.clear()
print(a)
del a





