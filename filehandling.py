# x=open("handling.txt","x")
y=open("handling.txt","w")
y.write("she is a student\n")
y.write("she is studying data analyst\n")
y.close()
y=open("handling.txt","a")
y.write("she is studying in futura labs")
y.close()
y=open("handling.txt","r")
z=y.read()
print(z)
y.close()
y=open("handling.txt","r")
print(y.read(6))
y.close()
y=open("handling.txt","r")
print(y.readline())
print(y.readline())
y.close()
# z=open("module2.txt","x")
import os
# os.remove("module2.txt")
os.rmdir("module3")








