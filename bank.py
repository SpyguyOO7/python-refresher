class Account:
    def __init__ (self,balance,name,number):
        """takes in balance, name, and account#"""
        self.balance = balance
        self.name = name
        self.number = number
        #self.e = 9
    def withdraw(self, amount):
        """Subtracts amount specifed from balance"""
        if amount < 0 or self.balance - amount < 0: #raise an error and stop the function if something is wrong
            raise ValueError('Amount drawn or resulting balance < 0')
            return
        self.balance -= amount

    def deposit(self, amount):
        """adds amount specifed to balance"""
        if amount < 0 : #raise an error and stop the function if something is wrong
            raise ValueError('Amount depositied < 0')
            return
        self.balance += amount

    def __str__(self):
        return (f'Balance: {self.balance} name: {self.name} account #: {self.number}')
#print("test on main!")

if __name__ == "__main__":#run only if this file is __main__
    print("test on main!")
    
