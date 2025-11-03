# x=open("file1.txt","x")
y=open("file1.txt","w")
y.write("python is a programming language")
y.close()
y=open("file1.txt","r")
z=y.read()
print(z)
y.close()
# a=open("file2.txt","x")
b=open("file2.txt","w")
b.write(z)



