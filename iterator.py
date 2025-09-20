
# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().


#-------Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.


mytuple = ("Apple", "Banana", "Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# ------ Even strings are iterable objects, and can return an iterator:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
    
mystr = "banana"
for x in mystr:
  print(x)
  
  
  
  
# ----------- Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# ------- StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)