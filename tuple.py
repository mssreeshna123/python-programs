x=("red","blue","yellow","black","green")
print(x)
print(type(x))
print(len(x))
print(x[2])
print(x[3:5])
print(x[1:])
print(x[:2])
print(x[-4])
print(x[-5:-3])
print(x[-3:])
print(x[:-2])
print("red"in x)
print("red"not in x)
for i in x:
    print(i)
y=list(x)
print(y)
y.insert(1,"green")
print(y)
y.append("yellow")
print(y)
y.pop(4)
print(y)
y[2]="white"
print(y)
x=tuple(y)
print(x)
a=("rose","sunflower","jasmine")
print(x+a)
b=a*2
print(b)
print(b.count("rose"))
b=("blue",)
print(b)
print(type(b))










