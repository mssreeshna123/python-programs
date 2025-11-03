# class name:
#     x="sreeshna"
# obj=name()
# print(obj.x)

# class Person:
#     def __init__(self,name,age):
#         self.fname = name
#         self.fage = age

# p1 = Person("Emil", 36)

# print(p1.fname)
# print(p1.fage)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name + "and I am",self.age,"years old")

# p1 = Person("Emil", 25)
# p1.greet()

#INHERITANCE
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)


# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

#POLYMORPHISM
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
  