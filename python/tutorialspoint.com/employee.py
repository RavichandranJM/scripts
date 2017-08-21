#! /usr/bin/python

class Employee(object):
    employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees += 1
    def total(self):
        print("Total employees {}".format(Employee.employees))
    def display(self):
        print("Name: {}, Salary: {}".format(self.name, self.salary))
emp1 = Employee("ravi", 10000)
emp2 = Employee("chand", 5000)
emp1.display()
emp2.display()
print "Total: {}".format(Employee.employees)
emp1.age = 10
print "Emp1 age: {}".format(emp1.age)
print getattr(emp2, 'name')
print hasattr(emp1, 'salary')
print setattr(emp2, 'name', 'jm')
print delattr(emp1, 'age')
emp1.display()
emp2.display()
print Employee.__dict__
print Employee.__doc__
print Employee.__name__
print Employee.__module__
print Employee.__bases__


