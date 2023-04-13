def generate_tax(income,percentage):
    tax = income *percentage/100
    return tax
# my_tax = generate_tax(2500,15)
# print(my_tax)
# A module is a file containing a set of codes or a set of functions which can be 

def names(first,second,age):
    full_name = (f'my first name is{first} and my surname is{second} i am {age} years old')
    return full_name
# name_age = names(' Taiwo',' Odubanjo ',26)
# print(name_age)

def print_pattern(n):
    for i in range(n+1):
        print('*'*i)
print_pattern(8)

# def print_name(**a):
#     return f" My name is {a['fname']{a['lname']}, i am {a['age']}} years old."
# print(name('Taiwo','Odubanjo',26))

'''
Import Built-in Modules
Like other programming languages we can also import modules by importing the file/function using the key word import. Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re'''

#Math Module 
'''import math
print(math.pi)
print(math.floor(math.sqrt(25)))
print(math.sqrt(25))
#rap up the own number
print(math.ceil(math.sqrt(243)))
#power
print(math.pow(2,5))
print(math.log10(100))'''

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
#statistics
from statistics import mean, median, mode,variance, stdev
age = [20,15,35,40,1,28,30,20]
print(mean(age))
def cal_mean():
    return mean(age)
print(cal_mean())

print(median(age))
def cal_median():
    return median(age)
print(median(age))

print(mode(age))
def cal_mode():
    return mode(age)
print(cal_mode())

age.sort()
print(age)

range_number =max(age)- min(age)
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


'''import random, string
print(string.digits, type(string.digits))
def OTP_genrator():
    chart_num = int(input('Enter a  number: '))
    num_OTPs = int(input('Number of OTPs to generate: '))
    for i in range(chart_num+1):
        OTP = ' '.join(random.choices(string.ascii_uppercase + string.digits, k= num_OTPs))
        # OTP = ' '.join(random.choices(string.ascii_uppercase + string.digits, k= 6))
        # OTP = 'ABC '.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        print(f"here is your OTP: {OTP}")
OTP_genrator()'''


# random, randint
# re

'''
Regular Expressions
A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.

The re Module
After importing the module we can use it to detect or find patterns.

import re
'''

import re 
# re.match()
txt = "I Iove Techstudio and Python"
# match_it = re.match('I Iove' ,txt)
# match_it = re.match('Techstudio' ,txt[7:])
match_it = re.match('studio' ,txt[7:])
print(match_it)

# re. search
search_it = re.search("Python",txt,re.I)
print(search_it)

# re.findall
txt2 = 'Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language. '
match_py = re.findall('python',txt2,re.I)
match_py = re.findall('python',txt2)
print(match_py)

#re.sub
sub_py = re.sub('Python|python', 'Javascript',txt2)
print(sub_py)
sub_py = re.sub('[Pp] ython', 'Javascript',txt2)
print(sub_py)

regex_pattern = r'first'
my_regex_match = re.findall(regex_pattern,txt2,re.I)
print(my_regex_match)

regex_pattern = r'LANGUAGE'
my_regex_match = re.findall(regex_pattern,txt2,re.I)
print(my_regex_match)


'''Assignment
Change the dictionary "person_dict" to a JSON "person_json". 
a) Print(person_dict)
b) Print(type(person_dict))
c) Print(person_json)
d) Print(type(person_json))'''
person_dict = {
    "name": "Blard",
    "country": "Nigeria",
    "city": "Lagos",
    "skills": ["JavaScrip", "React", "Python"]
}
import json
print(person_dict)
print(type(person_dict))
# to change dictionary to jsob you hhave to use json.dumps()
person_json=json.dumps(person_dict)
print(person_json)
print(type(person_json))

# to change json back to dictionary you use json.loads()
new_person = json.loads(person_json)
print(new_person,type(new_person))

# class Person3:
#     def _init_(self,name,age):
#         self.name = name
#         self.age = age
        
# person2 = Person3("Taiwo",23)
# print(person2.name)


