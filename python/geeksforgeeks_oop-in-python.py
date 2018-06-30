
'''  
class CSStudent:
    stream = "cse"
    
    def __init__(self, roll):
        self.roll = roll
    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return self.address
        
a = CSStudent(101)
b = CSStudent(102)
print CSStudent.stream
print a.roll
print a.stream
a.setAddress("Noida, UP")
a.getAddress()
'''
'''
class MyClass:
    __Hidden = 0
    def add(self, inc):
        MyClass.__Hidden += inc
        print MyClass.__Hidden

c = MyClass()
c.add(2)
c.add(5)
print c._MyClass__Hidden
'''
'''
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


t = Test(2, 3)
print(t)
'''
'''
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

a = Person("ravi")
b = Employee("chandran")
print a.isEmployee()
print b.isEmployee()
'''
'''
class Base:
    pass

class Derived(Base):
    pass

a = Base()
b = Derived()

print issubclass(Derived, Base)
print issubclass(Base, Derived)

print isinstance(a, Derived)
print isinstance(b, Base)
'''
'''
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print "str1"

class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print "str2"

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
    def printStrs(self):
        print (self.str1, self.str2)

d = Derived()
d.printStrs()
'''
'''
class Base(object):
    def __init__(self, x):
        self.x = x
class Derived(Base):
    def __init__(self, x, y):
        Base.x = x
        self.y = y
    def printXY(self):
        print (Base.x, self.y)
d = Derived(10, 20)
d.printXY()
'''
'''
class Base(object):
    def __init__(self, x):
        self.x = x
class Derived(Base):
    def __init__(self, x, y):
        super(Derived, self).__init__(x)
        self.y = y
    def printXY(self):
        print (self.x, self.y)

d = Derived(10, 20)
d.printXY()
'''
'''
class Base(object):
    def __init__(self, a):
        self.num = a
    def double(self):
        self.num = self.num * 2
    def printnum(self):
        print self.num
class Derived(Base):
    def __init__(self, a):
        super(Derived, self).__init__(a)
    def triple(self):
        self.num = self.num * 3
d = Derived(4)
d.printnum()
d.double()
d.printnum()
d.triple()
d.printnum()
'''
class Base(object):
    def __init__(self, name):
        self.name = name
    def isEmp(self):
        return False
    def getName(self):
        return self.name
    
class Derived(Base):
    def __init__(self, name, eid):
        super(Derived, self).__init__(name)
        self.eid = eid
    def isEmp(self):
        return True
    def getEid(self):
        return self.eid
d = Derived("Geek1", 101)
print d.isEmp(), d.getName(), d.getEid()
        

        
        


        
