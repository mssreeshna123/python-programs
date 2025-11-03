x={"name":"anu","place":"idukki","age":"18","course":"data science","duration":"4 month"}
print(x)
print(type(x))
print(len(x))
print(x["age"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
print("age"in x)
print("age"not in x)
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
x["age"]=23
print(x)
x.update({"place":"kollam"})
print(x)
x["instituiton"]="futura labs"
print(x)
x.update({"time":11})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("age")
print(x)
x.popitem()
print(x)
del x["instituiton"]
print(x)
x.clear()
print(x)
del x
berries={"berry1":{"name":"strawberry","amount":"15"},
         "berry2":{"name":"blueberry","amount":"25"},
         "berry3":{"name":"mulberry","amount":"35"}}
print(berries)
print(type(berries))
print(len(berries))
print(berries["berry3"])
print(berries["berry3"]["name"])





