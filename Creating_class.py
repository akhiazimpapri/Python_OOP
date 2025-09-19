class Myclass:
    x = 5
    
p = Myclass()
print(p.x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Akhi", 24)
# print(p2.name)
# print(p2.age)
print(p1) #<__main__.Person object at 0x100799fa0>

# The __str__() method controls what should be returned when the class object is represented as a string.

# If the __str__() method is not set, the string representation of the object is returned:


class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}"

p2 = Person2("Akhi", 24)
print(p2)


# Create own Methods
class Person3:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def myfunc(self):
        # print("HELLO " + self.name)
        return f"Hello {self.name}"

p3 = Person3("Akhi", 24)
# p3.myfunc()
print(p3.myfunc())
p3.age = 40 #Modify Object Properties
print(p3.age)


# Delete the age property from the p1 object:
# del p1.age

# Delete Objects
# del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person4:
  pass