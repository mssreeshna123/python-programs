x={"name":"sreeshna","age":21,"course":"data analytics","place":"vadavucode"}
print(x)
print(type(x))
print(len(x))
print(x["age"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
print("name"in x)
print("name"not in x)
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
x["age"]=25
print(x)
x.update({"place":"ernakulam"})
print(x)
x["duration"]="6 months"
print(x)
x.update({"instituition":"futura labs"})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("age")
print(x)
x.popitem()
print(x)
del x["duration"]
print(x)
x.clear()
print(x)
del x
family={"child1":{"name":"anu","age":20},
        "child2":{"name":"appu","age":15},
        "child3":{"name":"achu","age":13},
        }
print(family)
print(type(family))
print(len(family))
print(family["child2"])
print(family["child2"]["name"])


print("new content added")

print("updated from git")






      
