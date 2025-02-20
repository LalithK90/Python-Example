class Employee:
"""Common base class for all employees"""
empCount = 0

def __init__(self, name, salary):
self.name = name
self.salary = salary
Employee.empCount += 1

def displayCount(self):
print("Total Employee %d" % Employee.empCount)

def displayEmployee(self):
print("Name : ", self.name, ", Salary: ", self.salary)

# he variable empCount is a class variable whose value is shared among all instances of a this class. This can be
# accessed as Employee.empCount from inside the class or outside the class.
#
# The first method __init__() is a special method, which is called class constructor or initialization method that
# Python calls when you create a new instance of this class.
#
# You declare other class methods like normal functions with the exception that the first argument to each method is
# self. Python adds the self argument to the list for you; you do not need to include it when you call the methods.
