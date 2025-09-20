# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

#----- Creating a parent class
class Person:
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("Akhi Azim", "Papri")
x.printname()


#------ Create a Child Class
class Student(Person):
    def __init__(self, fname, lname):  #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function. The child's __init__() function overrides the inheritance of the parent's __init__() function.
        #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        Person.__init__(self, fname, lname)
#Use the Student class to create an object, and then execute the printname method:
x = Student("Kowsar", "Hossain")
x.printname()



#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()


#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.