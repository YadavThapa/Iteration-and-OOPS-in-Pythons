#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Iteration in Python
x = [6, 3, 1]
y = [ i**2 for i in x ]   # List Comprehension expression
print(y) 


# In[8]:


x = [6, 3, 1]
s = iter(x)


# In[9]:


print(next(s))      
print(next(s))      
print(next(s)) 


# In[10]:


count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)


# In[11]:


class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
  
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


# In[12]:


class Car:

    def __init__(self, name, mileage):
        self.__name = name              #private variable        
        self.mileage = mileage 

    def description(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage}km/l"


# In[13]:


# Calling class withour object
class Person:
    pass


# In[14]:


# Creating the Object 'p1'
class Person:             
    pass                    
p1 = Person()      # Creating the object 'p1'
print(p1) 


# In[15]:


class Person:
    pass
p1 = Person()
p1.fname = 'Jack'
p1.lname = 'Simmons'
print(p1.fname, '-', p1.lname)  # -> 'Jack - Simmons'


# In[16]:


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
p1 = Person('George', 'Smith')   
print(p1.fname, '-', p1.lname) 


# In[17]:


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
p1 = Person('George', 'Smith')   
print(p1.fname, '-', p1.lname)           # -> 'George - Smith'


# In[18]:


class Person:
    'Represents a person.'
    def __init__(self, fname, lname):
        'Initialises two attributes of a person.'
        self.fname = fname
        self.lname = lname


# In[19]:


help(Person)


# In[21]:


class MySubClass:   
   pass


# In[22]:


class MySubClass(object):   
    pass   


# In[23]:


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)


# In[24]:


p1 = Person('George', 'smith')
print(p1.fname, '-', p1.lname)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('John', 'williams', 123656)
print(e1.fname, '-', e1.empid)
print(e2.fname, '-', e2.empid)


# In[25]:


class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in Employee.all_employees:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees


# In[26]:


class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)

e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('George', 'Brown', 656721)
print(Employee.all_employees.search('or'))


# In[27]:


class Employee(Person):
    all_employees = EmployeesList ()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
    def getSalary(self):
        return 'You get Monthly salary.'
    def getBonus(self):
        return 'You are eligible for Bonus.'


# In[30]:


class ContractEmployee(Employee):
    def getSalary(self):
        return 'You will not get Salary from Organization.'
    def getBonus(self):
        return 'You are not eligible for Bonus.'
e1 = Employee('Jack', 'simmons', 456342)
e2 = ContractEmployee('John', 'williams', 123656)
print(e1.getBonus())
print(e2.getBonus())


# In[31]:


class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.__empid = empid
        Employee.all_employees.append(self)
    def getEmpid(self):
        return self.__empid


# In[32]:


e1 = Employee('Jack', 'simmons', 456342)
print(e1.fname, e1.lname)
print(e1.getEmpid())
print(e1.__empid)


# In[33]:


try:
    a = pow(2, 4)
    print("Value of 'a' :", a)
    b = pow(2, 'hello')   # results in exception
    print("Value of 'b' :", b)
except TypeError as e:
    print('oops!!!')
print('Out of try ... except.')


# In[34]:


try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise TypeError('Two inputs must be integers.')
    c = a**b
except TypeError as e:
    print(e)


# In[35]:


class CustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)


# In[38]:


try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise CustomError('Two inputs must be integers.')
    c = a**b
except CustomError as e:
    print(e)


# In[39]:


def divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Dividing by Zero.")
    finally:
        print("In finally clause.")


# In[41]:


class class_name:
    pass


# In[43]:


class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
  
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


# In[44]:


class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
          
    def speak(self):
        print("My name is {}".format(self.name))
  
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class methods
Rodger.speak()
Tommy.speak()


# In[45]:


# Python code to demonstrate how parent constructors
# are called.
  
# parent class
class Person(object):
  
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
  
    def display(self):
        print(self.name)
        print(self.idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
      
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
  
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
  
  
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
  
# calling a function of the class Person using
# its instance
a.display()
a.details()


# In[46]:


class Bird:
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        print("Ostriches cannot fly.")
  
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()


# In[48]:


# Python program to
# demonstrate private members
  
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class
class Derived(Base):
    def __init__(self):
  
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
  
  
# Driver code
obj1 = Base()
print(obj1.a)
  
# Uncommenting print(obj1.c) will
# raise an AttributeError
  
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
#Output


# In[52]:


class myClass():

    def method1 (self):
       print ('Guru99')
    def method2 (self,someString): 
       print ('Software Testing:') + someString


# In[53]:


# Example file for working with classes
class myClass():
  def method1(self):
      print("Guru99")
        
  def method2(self,someString):    
      print("Software Testing:" + someString)
  
      
def main():           
  # exercise the class methods
  c = myClass ()
  c.method1()
  c.method2(" Testing is fun")
  
if __name__== "__main__":
  main()


# In[54]:


class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))


# In[118]:


class Cadbury:
    def __init__(self,name,price):
        self.price = price
        self.name = name

    def display(self):
        print(self.price,self.name)

obj1 = Cadbury("DairyMilk",100)
obj1.display();


# In[59]:


class Employee:
    pass


# In[60]:


harry = Employee()
rohan = Employee()


# In[61]:


harry.fname ="harry"
harry.lname = 'jackson'
harry.salary = 4400

rohan.fname = "rohan"
rohan.lname = "das"
rohan.salary = 4400


# In[62]:


#Retrieve the first name of both employees.
print(harry.fname)
print(rohan.fname)

#Retrieve the last name of both employees.
print(harry.lname)
print(rohan.lname)

#Retrieve the salary of both employees.
print(harry.salary)
print(rohan.salary)


# In[63]:


def __init__(self):
    pass


# In[64]:


def __init__(self,fname,lname,salary):  
        pass  


# In[65]:


class Employee:
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary


# In[66]:


harry = Employee("harry","jackson",4400)
rohan = Employee("rohan","das",4400) 


# In[67]:


print(harry.fname)
print(rohan.fname)
print(harry.lname)
print(rohan.lname)
print(harry.salary)
print(rohan.salary)  


# In[68]:


class Employee:
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary

# Initializing the object
harry = Employee("harry","jackson",4400)
rohan = Employee("rohan","das",4400)


print(harry.fname,rohan.fname)


# In[69]:


class MyClass:
  x = 5


# In[70]:


print(x)


# In[71]:


print x


# In[75]:


class MyClass:
    a = 10
    b = 20


# In[77]:


def add():
    sum = a+b
print(sum)


# In[78]:


class MyClass:
       a = 10
       b = 20 
#Accessing variable present inside MyClass
print(MyClass.a)


# In[79]:


class MyClass:
       a = 10
       b = 20
       def add(self):
              sum = self.a + self.b
              print(sum)
 
#Creating an object of class MyClass
ob = MyClass()
 
#Accessing function and variables present inside MyClass using the object
print(ob.a)
print(ob.b)
ob.add() 


# In[87]:


class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)


# In[88]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# In[89]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# In[90]:


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# In[93]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# In[94]:


class Student(Person):
  pass


# In[95]:


x = Student("Mike", "Olsen")
x.printname()


# In[99]:


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x1 = Student("Mike", "Olsen", 2019)


# In[100]:


print(x)


# In[101]:


x1.printname()


# In[102]:


class A:
    def __init__(self):
        print("__init__ has been executed!")

x = A()


# In[103]:


class Robot:
 
    def __init__(self, name=None):
        self.name = name   
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
    

x = Robot()
x.say_hi()
y = Robot("Marvin")
y.say_hi()


# In[105]:


class Robot:
 
    def __init__(self, name=None):
        self.name = name   
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
    

x = Robot()
x.say_hi()
y = Robot("Marvin")
y.say_hi()


# In[107]:


class bus:  
    def __init__(self,model name, yr):  
    self.modelname = model name  
    self.yr= yr
    def display(self):  
        print(self.modelname,self.yr)    
c1 = bus("Tata", 2018)  
c1.display() 


# In[109]:


class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
c1 = car("Toyota", 2016)  
c1.display()  


# In[112]:


class employee():
    def __init__(self,name,age,id,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
 
emp1 = employee("harshit",22,1000,1234)
emp2 = employee("arjun",23,2000,2234)
print(emp1.__dict__)


# In[115]:


class employee1():
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee(employee1):
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
        emp1 = employee1('harshit',22,1000)
 
print(emp1.age)


# In[117]:


class employee1():
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class employee2():
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
 
class childemployee(employee1,employee2):
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
emp1 = employee1('harshit',22,1000)
emp2 = employee2('arjun',23,2000,1234)
 
print(emp1.age)
print(emp2.id)


# In[ ]:




