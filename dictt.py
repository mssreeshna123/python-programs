x={"name":"anu","place":"kollam","age":13,"course":"digital marketing"}
print(x)
print(type(x))
print(len(x))
print(x["name"])
print(x.get("age"))
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
x["age"]="15"
print(x)
x.update({"name":"appu"})
print(x)
x["duration"]="6 month"
print(x)
x.update({"instituition":"futura labs"})
print(x)
x.pop("age")
print(x)
del x ["course"]
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.popitem()
print(x)
x.clear()
print(x)
del x
fruits={"berry1":{"name":"strawberry","quantity":15},
        "berry2":{"name":"mulberry","quantity":25},
        "berry3":{"name":"blueberry","quantity":35}}
print(fruits)
print(type(fruits))
print(fruits["berry1"])
print(fruits["berry2"]["name"])


