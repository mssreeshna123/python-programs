x=["red","green","yellow","blue","black"]
print(x)
print(type(x))
print(len(x))
print(x[3])
print(x[2:4])
print(x[3:])
print(x[:4])
print(x[-2])
print(x[-5:-2])
print(x[:-3])
print(x[-2:])
print("blue"in x)
print("blue"not in x)
for i in x:
    print(i)
x[2]="red"
print(x)
x.append("white")
print(x)
x.insert(4,"orange")
print(x)
y=["rose","jasmine","sunflower"]
x.extend(y)
print(x)


