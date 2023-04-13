print('====NUMBER====')
# Number Data type
# num1 = 10
# gravity = 9.81
# com_num = 2j
# print(num1,gravity,com_num)
# print(num1, type(num1))
# print(gravity,type(gravity))
# print(com_num,type(com_num))
# num3 = str(num1)
# print(num3)
# print(num3,type(num3))
# age = 28
# my_sum = num1 + int(num3)  -int(age)
# print(my_sum)

#formatting  f methods
a = 4
b = 3

num_sum = print(f'The sum of { a} and {b} is {a + b}')
print('the sum of {} and {} is {}'.format(a,b, a + b))
# print(num_sum)

#Task one 
S = 'My name is fred, a fullstack developer'
print(S.split(',') [0])
print(S.split(',')[1].strip().capitalize())

x, y = '8' , 5
print(x,y)
print(x, type(x))
print(y, type(y))
print(x *y)
print(x * 3)

print(int(x)*3)
print(int(x)*y)

y,x ='8' ,5
print(x)
print(y)

tech_stack = 'html,css,javascript, python,node'
front_end = tech_stack.upper().split(',')
back_end = tech_stack.title().split(',')
print(front_end)
print(back_end[3],back_end[4])

#Boolean
a = 5
b = 10
c = '5'

print(a == b)
print(a < b)
print(a > b)
print(a == c)
print(type(a == c))

#Operators
# 1 ASSIGNMENT OPERATOR =, < , >, +=, -+, *=, <=, >=
x = 8
y = 3
if x < y:
    print(x+y) 
else:
    print(y-x)


#ARITHEMETIC OPERATORS +,-, *, /, //, FLOODLESS %,**,EXPONENTIAL
    m = 7
    n = 25
    p = -4
    print(n+m-p**2/6*2)
    print(n+m-p**2//6*2)
    print(n/m)
    print(n//m)
# comparrism operator example
    if n !=p:
        print('n is not a factor of p')
    else:
        print('we are good')
    
    if n%m == 0:
        print('m is a factor of n')
    else:
        print('wahala! '* 3)
    #LOGICAL OPERATOR and, or, not,
        j = 3
        k = 8
        l = -2
        z= 6
    _try = (k>j) and (l<k)
    print(_try)
    do_math = (k+l or k) > (k+j)
    print(do_math)
    do_math = (k+l or k) == (z)
    print(do_math)
    if _try:
        print("We're good!")
    else:
        print("Wahala dey oo!")
        
        if not _try:
            print("We're good!")
        else:
            print("Wahala dey oo!")


    # input()
    # name = input('What is your name:')
    # print(name)
    
    def _sum(a,b):
        print(a+b)
    _sum(2,3)
        # def _sum(a,b):
        #     print(a+b)
        #     _sum(2,3)
        
    # def sth():
    #     num1 = int(input('Enter first number: '))
    #     num2 = int(input('Enter second number: '))
    #     print(num1 + num2)
    # sth()
    
    # def calc_rec_area():
    #     length = int(input('Enter first number: '))
    #     breadth =int(input('Enter second number: '))
    #     area = length*breadth
    #     print(f'The area of the rectangle is {area}cm^2')
    # calc_rec_area()
    
    # lists data type
    print('===LIST===')
    # List is a collection of items/ (any data type() in a squared bracket []
    # i. e array
    my_arr = list()
    '''print(type(my_arr))'''
    
    '''List = ['strings',25,9.8,True,[2,3],(1,2,5)]'''
        # List method index, slice, len
        # len()
    # print(len(List))
    
    #pop() pop is a method
        # print(List.pop())
    '''a,b,c,*rest,d = List'''
    # print(a)
    # print(b)
    # print(c)
    # print(rest)
    # print(d)
    '''print(List[4:])'''
    
    # Slicing [start:end]
    '''new_List = List[-2:]
    print(new_List)
        
    print(new_List[0][1])
        
    rev_List = List[-6:]
    print(rev_List)
        
    rev_List = List[::-1]
    print(rev_List)'''
    
    # class work
    fruits =['banana', 'orange', 'mango', 'lemon']
    # print(fruits[0],fruits[2])
    # print(fruits[::2])
    # print(fruits[1::2])
    # print(fruits[0::3])
    # # print(fruits[::-2])
    
    
    # Task 1
scores = [22, 19, 24, 25, 26, 24, 25, 24,15]
'''
a) Arrange the scores in ascending order
b) Arrange the scores in descending order
c) Print the even scores Hint: use list comprehension
d) Print only the maximum score
e) Print only the minimum score

'''
'''Ascending order'''
scores.sort()
print(scores)

#decending order
scores.sort(reverse=True)
print(scores)
#maximum
Max_num = max(scores)
print(Max_num)
#mminimum
min_num = min(scores)
print(min_num)


'''List Comprehension'''
'''for i in scores:
    if i%2==0:
        print(i)'''

# Task 2
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
a) Join the two lists above and store in a variable my_stacks
b) Copy the joined list and assign it to a variable full_stack.
c) Then insert 'Python' and SQL after 'Redux'.
'''
my_stack = front_end + back_end
print(my_stack)

print(len(scores))
mid_index = len(scores)/2
print(mid_index)
mid_index = len(scores)//2
print(mid_index)
median_score = print(scores[mid_index])

'''List Comprehension'''
my_stacks = front_end  + back_end
'''print(my_stacks)
            
front_end.extend(back_end)
print(front_end) 

back_end.extend(front_end)
print(back_end)

print(scores.count(24))
'''
print(scores.count(24))

add_stack = ['Python', 'SQL']
all_stack =front_end + add_stack + back_end 
print(all_stack)

# my_stacks.insert(5,'python')
# print(my_stacks)

add_stacks = my_stacks.index('Redux')
my_stacks.insert(add_stacks +1,'Python')
my_stacks.insert(add_stacks +2,'SQL')
print(my_stacks)

# Tuple 
# Tuple are collection of data type in python are another version of list they are declared in a parentheses ()
# Tuple is one of the four collection/sequence data type in python
#Tuple or tuple constructor function Tuple, tuple allow duplication.
tpl1 = tuple(())
print(tuple)
tpl = ('string', -3,True)
print(tpl1, type(tpl1))
tpl1 = tuple((2, 'baby', 2))
print(tpl1, type(tpl1))
#accessing tuple
print(tpl[2])
#len()
print(len(tpl1))

# Udating tuples, tuples is in editable
# tpl1.append('sth')
tpl1_lst = list(tpl1)
print(tpl1_lst)
tpl1_lst[0] = 'item1'
print(tpl1_lst)
tpl1_lst.insert(1,'item1')
print(tpl1_lst)
print(tpl1_lst),type(tpl1_lst)



def example_function():
    print('This is a function')
example_function()

def add_number():
    num1 = 3
    num2 = 2
    total_num = num1 + num2
    print(total_num)
add_number()

# class work
# A = PI*r**2 PI = 3.142
# when r = 3.5
def cal_area():
    Pi = 3.142
    r = 3.5
    A = Pi*r**2
    print(A)
cal_area()

def cal_area1(r, PI =3.142):
    A = PI * r**2
    print(A)
cal_area1(3.5)

def cal_area1(r, PI):
    A = PI * r**2
    print(int(A))
cal_area1(3.142,3.5)

## function with parameters
def full_name(first_name,last_name):
    print(f'my name is {first_name}{last_name}')
full_name('Blard', ' Omu')

def sum_numbers(n):
    total = 0
    for i in range(n+1):
        total +=   i
    print(total)
sum_numbers(10)
print(sum_numbers(100))



# Arbitrary arguments, *arg
siblings = ['kehinde','Taiwo','Idowu','dami','Abbey']
def my_stack():
    for name1 in siblings:
        print(f'my name is {name1}')
my_stack()

def my_siblings(*b):
    print(f'The youngest child is {b[4]}')
    print(f'The Techie child is {b[2]}')
    print(f'The foodie child is {b[3]}')
my_siblings('kehinde','Taiwo','Idowu','dami','Abbey')

# keyword arguments **arg
#key1 = value
def myCal(l,b,h):
    Vol = l*b*h
    print(f'Vol is {Vol}cm^3')
myCal(4,6,2)

def myCal(l,b,h):
    Vol = l*b-h
    print(f'Vol is {Vol}cm^3')
myCal(l=4,b=6,h=2)

def myCal(**k):
    print('This is ' + k['key3'])
    print('This is ' + k['key1'])
    print('This is ' + k['key2'])
    print(f"'This is ' + {k['key2']}")
myCal(key3='Taiwo',key2='praise',key1='kenny',key4='Oyin')

#return statement
def my_return(first, second):
    return f'My name is {first} {second}'
print(my_return('Blard','Omu'))

def do_sum(a,b):
    return a+b*a-b
print(do_sum(5,6))

def do_pass():
    #empty
    pass
do_pass()

# continue
fruits = ['apple','orange','mango','pineapple','grape']
def fav_fruit():
    for fruit in fruits:
        if fruit == 'mango':
            continue
#         print(f'My favourite fruit is {fruit}')
# fav_fruit()

# class work
'''
create a function find_even_number such that print(find_even_number(20)) will 
print the even numbers between 1 and 20 and store it in a list
called evens
'''    
def even_num():     
    for i in range(1,21):
        if i %2 == 0:
            print((i) )
even_num()

def even_num(n):
    even = []
    for i in range(n+1):
        if i % 2 == 0:
            if i== 0 :
                continue
            even.append(i)
            return even
        print(even_num(20))
        
# lambda Function
# lambda args : expression
mySum = lambda a : a**2
print(mySum(5))

Vol_clinder = lambda p,r,h : p*r**2*h
print(Vol_clinder(3.142,7,4))

def generate_tax(income,percentage):
    tax = income*percentage/100
    return tax
my_tax = generate_tax(2500,15)
print(my_tax)
# A module is a file containing a set of codes or a set of functions which can be 

def name(first,second,age):
    full_name = (f'My name is {first} and my surname is {second} i am {age} years old')
    return full_name
total_nam = name('taiwo', 'Odubanjo',26)
print(total_nam)

def print_pattern(n):
    for i in range(n+1):
        print('*'*i)
print_pattern(8)
     
def name_name(**a):
    return f" my name is{a['fname']}{a['lname']} i am {a['age']}"
print(name('Taiwo','Odubanjo',26))

'''Import Built-in Modules
Like other programming languages we can also import modules by importing the file/function using the key word import. Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re'''

# math modules
import math
print(math.pi)
print(math.floor(math.sqrt(25)))
print(math.sqrt(25))
#rap up the own number
print(math.ceil(math.sqrt(245)))
# power
print(math.pow(2,5))
print(math.log10(100)) 

# from math import pi, ceiling importing only one math method
'''from math import pi, ceil, sqrt
print(pi)
print(ceil(sqrt(243)))
print(math.pow(2,5))
print(math.log10(100))


from random import random, randint,randbytes,randrange
print(random())
print(randint(2,6))
'''
     
# statistics
from statistics import mean, median, mode, variance, stdev
age = [20,15,35,40,1,28,30,20]
print(mean(age))

def cal_mean():
    return mean(age)
print(cal_mean())

print(median(age))
def cal_median():
    return median(age)
print(cal_median())

print(mode(age))
def cal_mode():
    return mode(age)
print(cal_mode())


age.sort()
print(age)

range_number = max(age)-min(age)
print(range_number)

def cal_range():
    range_number = max(age)-min(age)
    return range_number
print(cal_range())

print(variance(age))
def cal_variance():
    return variance(age)
print(cal_variance())

print(stdev(age))
def cal_standard():
    return stdev(age)
print(cal_standard())

import random, string
print(string.digits, type(string.digits))

# class Person:
#     def __init__(self,name,age):
#         self.name   = name
#         self.age    =  age
# path = Person('Esther',22)      
# print(f'My name is {path.name} i am {path.age} years old')

# class Person:
#     def __init__(self,fname,lname,age,city):
#         self.fname  = fname
#         self.lname  = lname
#         self.age    = age
#         self.city   = city
        
#     def person_info(self):
#         return f"my name is {self.fname} {self.lname}, i am {self.age} years old, i live in the {self.city}"
# p = Person("Taiwo",'Odubanjo',40,'Lagos')
# print(p.person_info())
        
        
        
        
class Person:
    def __init__(self,fname,lname,age,city,stack):
        self.fname  = fname
        self.lname  = lname
        self.age    = age
        self.city   = city
        self.stacks  = []
        return f"my name is {self.fname} {self.lname}, i am {self.age} years old, i live in the {self.city}"
    def add_stacks(self,para):
        new_lst = self.stacks.append(para)
        print(new_lst)
s = Person("Taiwo","Odubanjo",40,"Lagos")
print(s.stacks)
s.add_stacks = ("HTML")
print(s.stacks)

        
    



# import modules
# print(modules.generate_tax(2500,15))

# from modules import generate_tax as my_task
# print(my_task(2500,15))

# from modules import names as my_tase
# print(my_tase(' Taiwo',' Odubanjo ',26))


# from modules import generate_tax,print_name as about_me
# print(about_me(fname='kike',age=23,lname='Lomo'))



      
        
       
