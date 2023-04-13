# while run:
#     my_calc()
    
    
# OOP
# Classes
# Python is an object oriented programming language, with its properties and methods
# Everything in python is an object of a corresponding built-in class
# we instantiate a class to create an object,however the class defines the attributes and behaviour of the object,

# Creating an class
# To create a class, we use the 'class' keyword.

# class Classname:
    # codes to run
# class Person:
#     pass
# # print(Person)

# person1 = Person()
# print(person1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person4 = Person("Blard",39)
print(f'My name is {person4.name} and i am {person4.age} years old')
    
# class Person:
#     def _init_(self,fname,lname,age,city):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.city = city
#     def person_info(self):
#         return f"My name is {self.fname} {self.lname}, i am {self.age} years old. i live in {self.city}"
# p = Person("Blard","Omu",26,"Eko")
# print(p.person_info())

# class Person:
#     def __init__(self,fname,lname,age,city):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.city = city
#         self.stacks = []
        
#     def person_info(self, gender, income):
#         self.gender = gender
#         self.income = income
#         return f" My name is {self.fname} {self.lname}, i am {self.age} years old. i live in {self.city} and the list of my stacks are: {self.stacks}. My gender is {gender}, My net income is {income} "   
#     def add_stacks(self,para):
#        new_lst = self.stacks.append(para)
#         # print(new_lst)
# s = Person("Taiwo","Omu",26,"Eko")
# s.add_stacks('HTML')
# more_stacks =["css","Javascript","React","Python"]
# print(s.stacks)
# s.stacks.extend(more_stacks)
# print(s.stacks)
# print(s.person_info("Others",1200))




# # Class inheritance using the super()
# # The super() built-in function give child class access to the main/parent properties.However, when we add the init() function, the child class will no longer inherit the parant's init() function.

# class SmallPerson(Person):
#     def __init__(self,fname,lname,age,city,job):
#         self.job = job
#         super().__init__(fname, lname, age, city)
        
#     def new_info(self):
#             return f" my stack is {r.stacks} and my job is (r.job)"
        
#     pass
# r = SmallPerson("Praise", "Rashford",79,"Scotland","Fullstack dev")
# r.add_stacks("Djanjo")
# print(r.person_info("male", 1400))
# print(r.stacks)
# print(r.job)
# # print(r.age)
# print(r.new_info())



# Task
'''
1) Create a class 'BankAccount' with constructor that has two parameters, 'name' and 'money'
2) Create inside the BankAccount class three methods, one for 'deposit', 'withdraw', 'checkbalance'.
3) Create an instance of BankAccount. l.e b1 = Bankaccount("Blard",400)
4) Print (b1.withdraw(500)). Nb: This should show a message "Insufficient funds" since 400<500
5) Deposit 500 using b1.deposit(500) method and check the available balance using print(b1.checkbalance()) method.

'''

# Solution
class BankAccount:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
# Methods
    def deposit(self,value):
    # self.money = self.money + value
        self.money += value

    def withdraw(self,dec):
        if self.money > dec:
            self.money = self.money - dec
            return self.money
        else:
            return "Insufficient fund! you're a broke ass"
        
    def checkbalance(self):
        return self.money
        
        
    
    
b1 = BankAccount("Taiwo",400)
print(b1.money)
b1.deposit(500)
print(b1.money)
print(b1.withdraw(1500))
print(b1.checkbalance())
    
