#! /usr/bin/python
import classvar
class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "Initializing SchoolMember {}".format(self.name)
    def tell(self):
        print "Name: {}, Age: {}".format(self.name, self.age),
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print "Initializng student {}".format(self.name)
    def tell(self):
        SchoolMember.tell(self)
        print "Marks: {}".format(self.marks)
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print "Initializing teacher {}".format(self.name)
    def tell(self):
        SchoolMember.tell(self)
        print "Salary: {}".format(self.salary)

s = Student("ravi", 20, 78)
t = Teacher("raghu", 40, 30000)
s.tell()
t.tell()

