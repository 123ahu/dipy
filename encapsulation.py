class BankAccount:
    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited ksh", amount, "into account of ", self.__name, " New balance: ksh", self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print("Withdrew ksh", amount, " from account of ", self.__name, " New balance: ksh", self.__balance)

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name


account = BankAccount("John Doe", 1000)


account.deposit(500)
account.withdraw(200)


print("Account name:", account.get_name())
print("Account balance: ksh", account.get_balance())
