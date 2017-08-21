#! /usr/bin/python
class Account(object):
    def __init__(self, amt = 0):
        self.bal = amt
    def deposit(self, amt):
        self.bal += amt
        return self.bal
    def withdraw(self, amt):
        self.bal -= amt
        return self.bal
class MinBalAccount(Account):
    def __init__(self, amt):
        #super(MinBalAccount, self).__init__(amt)
        Account.__init__(self, amt)
        self.min_bal = 500
    def withdraw(self, amt):
        if (self.bal - amt) < self.min_bal:
            return "Cannot withdraw"
        else:
            return Account.withdraw(self, amt)
a =  MinBalAccount(1000)
b =  MinBalAccount(500)
c = Account(600)
print a.deposit(100)
print a.withdraw(50)
print b.deposit(50)
print c.withdraw(60)
print b.withdraw(510)
