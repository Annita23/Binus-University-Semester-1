# class Student:
#     def __init__(self, name, age, height, hobbies, major):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.hobbie = hobbies
#         self.major = major

#     def info(self):
#         print(f"Student information are: \nName: {self.name}, Age: {self.age}, Height: {self.height} cm. Student major is {self.major}.")

#     def eat(self):
#         print(f"{self.name} is eating nasi goreng.")

#     def sleep(self):
#         print(f"{self.name} is sleeping.")

#     def study(self):
#         print(f"{self.name} is studying Computer Science.")

#     def hobbies(self):
#         print(f"{self.name} hobbies are: {self.hobbie}")


# a1 = Student("Annita", 21, 164, "badminton,basketball, music", "Computer Science")
# a1.info()
# a1.hobbies()


class BankAccount:
    bank_name = "BCA"
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposite amount is {amount}. {self.owner}'s updated balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds from {self.owner} account.")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"The current balance of {self.owner} account is: {self.balance}")


account1 = BankAccount("Amie", 1000)
account1.deposit(867)
account1.withdraw(100)
account1.show_balance()
account1.withdraw(2000)
account1.show_balance()
print("account1 bank name is:", account1.bank_name)

account2 = BankAccount("Annita", 5000)
account2.show_balance()
account2.deposit(2000)
account2.withdraw(1000)
account2.show_balance()