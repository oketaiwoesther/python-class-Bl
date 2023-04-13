# print("hello world")
# variables
'''name = 'Blard'
num = 2
num_2 = 9.83
print(name, num,num_2)
print(name)
print(num)
print(num_2)

full_name = name + "omu"
print(full_name)
a, b, c = 2, 'Onipanu', "Lagos"
print(a)
print(b)
print(c)
print(a, b, c)'''

# Data Types
'''-Strings
_Numbers e.g int, float, complex
_Sequence e.g Lists, sets, tuples
_Dictionary'''

#Strings
surname = 'Oluremi'
first_name = ' tade'
full_name1 = surname + first_name 
age = '24'
bmi = 68
# bmi = 7.68
print(surname, type(surname))
print(age, type(age))
print(bmi, type(bmi))
# print(first_name, type(first_name))


# String methods index, len, upper, lower, slice, endwith, startwith, title,#String formatting f, count
print(len(first_name))
print(len(surname))
print(surname[0])
print(surname[1])
print(surname[2])
print(surname[3])

print(surname[4])


# UPPER()
print(full_name1.upper())

# lower()
print(full_name1.lower())

# slice [start:end]
print(surname[0:3])
print(surname[3:8])
print(surname[3:8].capitalize())
print(full_name1[ :8])
print(full_name1[8:12])

acad = 'Techstudio'
print(acad[0:-6])
print(acad[4:10].capitalize())
#title ()
#mutipute change the first letters to upper
mult_str = 'My name is Taiwo, I love Python'
print(mult_str.title())
print(mult_str.startswith('n'))
print(mult_str.endswith('on'))

#count ()
# print(mult_str.count())


#String formatting f
more_str = print(f'{mult_str} and javascript {acad}')

# split()
print(mult_str.split(',')[0])
print(mult_str.split(','))
print(mult_str.split(' ')[3])


name = 'Taiwo'
course = "web developer"
age = 28
state = "Ogun state"
nationality = 'Nigeria'
details=print(f'My first is {name} i am {age} years old, i came from {state} i am {course} i am from {nationality}' )

# replace()
repl_word = 'i love python'
print(repl_word)
print(repl_word.replace('python', 'javascript'))



# print('====NUMBER====')
# # Number Data type
# num1 = 10
# gravity = 9.81
# com_num = 2j
# print(num1, gravity, com_num)
# print(num1, type(num1))
# print(gravity, type(gravity))
# print(com_num, type(com_num))
# num3 = str(num1)
# print(num3, type(num3))
# my_sum = num1 + int(num3)  -int(age)
# print(my_sum)

# a = 4
# b = 3

# num_sum = print(f'The sum of { a} and {b} is {a + b}')
# print('The sum of {} and {} is {}'.format(a, b, a + b))

#Task one 
S = 'My name is fred, a fullstack developer'
print(S.split(',')[0])
print(S.split(',')[1].strip().capitalize())

x, y = '8' , 5
print(x, type(x))
print(y, type(y))

print(x * 3)
print(x * y)

print(int(x)*3)
print(int(x)*y)

y,x ='8' ,5
print(x)
print(y)


tech_stack = 'html,css,javascript, python,node'
front_end = back_end = tech_stack.upper().split(',')
print(front_end)
print(front_end[0], front_end[1], front_end[2])
print(front_end[3].title(), front_end[4].title())



#Boolean
a = 5
b = 10
c = '5'

print(a == b)
print(a < b)
print(a > b)
print(a==c)
print(type(a==c))

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
        print(-_try)
        do_math = (k+l or k) > (k+j)
        print(do_math)
        do_math = (k+l or k) > (k-j)
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

        #COMPARISON OPERATIORS  ==, !=, >, <, >=, <=
        if (j!=k):
            print('Numbers are not equal')
            
            
            # input()
        # name = input('What is your name:')
        # print(name)
        
    
        def _sum(a,b):
            print(a+b)
        _sum(2,3)
        
        # def sth():
        #     num1 = int(input('Enter first number: '))
        #     num2 = int(input('Enter second number: '))
        #     print(num1 + num2)
        # sth()
            
        # def calc_rec_area():
        #         length = int(input('Enter first number: '))
        #         breadth =int(input('Enter second number: '))
        #         area = length*breadth
        #         print(f'The area of the rectangle is {area}cm^2')
        # calc_rec_area()
        
        # lists data type
        print('===LIST===')
        # List is a collection of items/ (any data type() in a squared bracket []
        # i. e array
        # my_arr = list()
        # print (type(my_arr))
        List = ['strings',25,9.8,True,[2,3],(1,2,5)]
        # List method index, slice, len
        # len()
        print(len(List))
        #pop()
        # print(List.pop())
        # unpacking of List
        a,b,c,*rest,d = List
        print(a)
        print(b)
        print(c)
        print(*rest)
        print(rest)
        print(d)
        print(List[4:])
        
        # Slicing [start:end]
        new_List = List[-2:]
        print(new_List)
        
        print(new_List[0][1])
        
        rev_List = List[-6:]
        print(rev_List)
        
        rev_List = List[::-1]
        print(rev_List)
        
        # class work
        # fruits =['banana', 'orange', 'mango', 'lemon']
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

# Task 2
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
a) Join the two lists above and store in a variable my_stacks
b) Copy the joined list and assign it to a variable full_stack.
c) Then insert 'Python' and SQL after 'Redux'.
'''
# Ascending order
scores.sort()
print(scores)

#Descending order
scores.sort(reverse=True)
# print(scores)

'''List Comprehension'''
'''for i in scores:
    if i%2==0:
        print(i)
''' 
 
 

        
# Maximum
max_num = max(scores)
# print(max_num)
# minimum
min_num = min(scores)
# print(min_num)

print(len(scores))
mid_index =len(scores)/2
print(mid_index)
mid_index =len(scores)//2
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
# add_stacks = ['Python', 'SQL']
# All_stack = front_end + add_stacks +back_end
# print(All_stack)  
  
# my_stacks.insert(5,'python')
# print(my_stacks)

add_stacks = my_stacks.index('Redux')
my_stacks.insert(add_stacks +1,'Python')
my_stacks.insert(add_stacks +2,'SQL')
print(my_stacks)

# Tuple 
# Tuple are collection of data type in python are another version of list they are declared in a parentheses ()
# Tuple is one of the four collection/sequence data type in python, tuple you have to convert it to list and use and then convert it back
#Tuple or tuple constructor function Tuple, tuple allow duplication.
tpl1 = tuple(())
tpl = ('string', -3,True)
print(tpl1, type(tpl1))
tpl1 = tuple((2, 'baby', 2))
tpl = ('string', -3,True)
print(tpl1, type(tpl1))
print(tpl[2])
# Accessing tuple
print(tpl[2])

#len()
print(len(tpl1))

# Udating tuples, tuples is in editable
# tpl1.append('sth')

tpl1_lst = list(tpl1)
print(tpl1_lst)
# tpl1_lst[0] = 'item1'
# print(tpl1_lst)
tpl1_lst.insert(1,'item1')
print(tpl1_lst)
print(tpl1_lst), type(tpl1_lst)

#change back to tuple
tpl1_lst = tuple(tpl1_lst)
print(tpl1_lst, type(tpl1_lst))
del tpl1_lst
# slicing
team = ('LVP','PSG','ARS','CHE','MAN')
print(team[1::2])
print(team[::4])

# SETS
# set is also a collection of data type but it's element are enclosed in a curly braces {} set is unordered, set does not duplicate that is not having two numbers or variable in two.
my_set = set({})
print(my_set)
print(type(my_set))
my_set1 = {'head', 7,'habit', False, 'Oyin'}
print(len(my_set1))
print(my_set1)
my_set2 = {'blue','yellow','green', 'red', 'black'}
#print ('green'in my_colors)
# updating sets undate()
add_color = {'purple', 'pink', 'white', 'blue'}
my_set2.update(add_color)
print(my_set2)
# Since set is not ordered or indexed, we can only access it via looping, however we can add and remove items from the set
# use .add() to add one item only
# use .update() to add multiple item.
# use .remove() to a spe
# cified item

# SETS
# Set is also a collection data type but it's element are enclosed in a curly braces {} 
# set is unordered, unindexed
# Once a set is created we cannot change any items but we can add additional items.
# Set does not recognize duplicate

# Creating sets
my_set = set({})
print(type(my_set))
my_colors = {'blue','yellow','green','red','black'}
print(my_colors)
# print('green' in my_colors)

# updating sets update()
add_color = {'purple', 'pink','white','blue'}
my_colors.update(add_color)
print(my_colors)
# Since set is not ordered or indexed, we can only access it via looping, however we can add and remove items from the set
# use .add() to add one item only
# use .update() to add multiple item.
# use .remove() to a spe
# cified item

new_data = {1,8,'black', True,False,0}
# print(new_data)

# adding one item add()
new_data.add(3)
# print(new_data)

# adding multiple items .update()
extra_items = {2,9,'hello'}
new_data.update(extra_items)
# print(new_data)

# removing item
# new_data.remove('black')
# print(new_data)

# pop() will remove random item and return the removed item
# clear() will clear will clear all the items, returns empty set
# del will delete the set whole set




#example of duplicate
new_data = {1,8, 'black',True,False,0}
print(new_data)
# to remove item from a set
new_data.remove('black')
print(new_data)
# you can not add to set but you can remove from it

#Conditional if, elif, for, range, while
a = 2
b = 7
if a < b:
    #print('Do you care for a drink?)
    # input('  ')
    '''input("Do you care for a drink?")
    print('Thanks boss!')
else:
    print('Nothing for you!')'''
    
'''    Write a program to accept an input of number and print either
    1 The number is even 
    2 The number is Odd'''
     

# w = [1,2,3,4,5,6,7,8,9,10,11]
# for x in w:
    # x =int(input('insert number'))
    # if x % 2 == 0 :
    #     print('even number')
    # else:
    #     print('odd number')
        
#using for loop
# for i in range(3):
#     try:
#         number = int(input('Enter an integer: '))
#         break
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
# else:
#     print("Max attempts reached. Exiting program ...")
#     exit()
    
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print(' The number is odd.')
    

a = 2
b = 3
if a > b:
    print('a is greater than b')
elif a == b:
    print('a is equal to b')
else:
    print('b is greater than a')
a = 3
b = 3
if a > b:
    print('a is greater than b')
elif a == b:
    print('a is equal to b')
else:
    print('b is greater than a')
    
    
#LOOPS FOR AND WHILE
# for Loop
'''for condition:
    //run code'''
'''cars = ['mercedes','Lexus', 'Toyota', 'BMW', 'Honda']
for car in cars:
    print(f' my favourite car is {car}')
    
for brand in cars:
    if brand =="Toyota" :
        print(f'my best brand is {brand}')
    
for brand in cars:
    my_best_car = "Lexus"
    print(f'my best car  is {my_best_car}')'''
    
    
    
clubs = ("ARS", "EVE", "MAN","LIV",'CHE')
for club in clubs:
     if "A" in club:
        print(club)
# Different between for and while
# for loops runs only onces, and while loops runs only if the conditional is trueOR percist
            
for w in range(11):
    print(w)
for double in range(1,20,2):
    print(double)
    
# while loop
i = True 
while i:
    print('while loop running...')
    break
y = 1
while y < 5:
    print('while loop running...')
    y += 1


cars = ['mercedes','Lexus', 'Toyota', 'BMW', 'Honda']
p = 2
while p <= 4:
    # print(f'This car brand is {cars[:3]}')
    # print(f'This car brand is {cars[p]}')
    p += 1
    
    
#Dictionary
#Dict is one of the four collection data type
# dict are key-value pair of data stored in a curly braces {}
dct = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':'value4',
    'address':{
        'No': 19,
        'street': 'Akeju'
    }
    
}

person_Detail ={
    'name': 'Esther',
    'age' : 27,
    'gender': 'female',
    'occupation': 'web developer',
    'state': 'Lagos',
    'dob': 2010,
    'fav_food': 'rice'
    
}
#it does not allow .get
#Accessing dict
print(dct['key1'])
print(dct.get('key3'))
print(dct['address'] ['street'])
str1 = dct['address']['street']
str_no = dct['address']['No']
print(str_no, str1)
print(dct['address'] ['No'],dct['address']['street'])

#Adding items to a dict
dct['key5'] = [1,2,3,True]
print(dct)
# how to check if a key exist in a dictionary
print('key4' in dct)

#Removing key-value from a dict
#it removed a specified key
dct.pop('key3')
print(dct)

# it remove the last item
# dct.popitem()
print(dct)
print(dct.popitem())
#remove the last item
#print(dct)

# dct.popitem()
# print(dct)
# you can remove with delete
# del dct[key]

#to get the list of keys in your dictionary
# print(dct.keys())

# Assignment
sister = ('Damilola','Kehinde','Idowu','Taiwo')
brother = ('Lekan','Abiodun','Juda')
siblings = sister + brother
print(siblings)
total_sb =len(siblings)
print(total_sb)
# Modify tuple
siblings_tuple = list(siblings)
print(siblings_tuple)

parent = ('Oyin','Jonathan')
siblings_tuple.extend(parent)
print(siblings_tuple)
# # upper()
lst3 = [x.upper() for x in siblings_tuple]
print(lst3)
# # unpack
a,b,c,d,e,f, *rest = lst3
print(a,b,c,*rest)
print(b)
print(c)
print(d)
print(e)
print(f)


# Excerise two
f = range(1, 100, 3)
for d in f:
    print(d)
    
for y in range(1,100,3):
    print(y)

# # exercise 3
# # Multiplication table (from 1 to 10) in Python

for count in range(0,11):
    multiply = count*count
    print(count,'X',count,'=',multiply)
# using while loop
n = 0
while n < 11:
    print(f'{n} x {n} = {n*n}')
    n = n + 1

num = 4

# To take input from the user
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1,11):
   print(num, 'x', i, '=', num*i)
   

for count in range(0,11,1):
    x = count + 1
    multiply = count*(x)
    print(count,'X',x,'=',multiply)
    
    
    
