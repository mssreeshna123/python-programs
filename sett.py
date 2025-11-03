x={"anu","ammu","amal","anju","appu"}
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)
print("anu" in x)
print("anu"not in x)
x.add("achu")
print(x)
y={"red","blue","green","anu","appu"}
x.update(y)
print(x)
z=x.union(y)
print(z)
a={"one","two","three","four","five"}
b={"blue","red","one","two","orange"}
c=a.intersection(b)
print(c)
d=a.difference(b)
print(d)
e=a.symmetric_difference(b)
print(e)
a.remove("one")
print(a)
a.discard("blue")
print(a)
a.pop()
print(a)
m=frozenset({1,2,3,4})
print(m)
print(type(m))
del m







