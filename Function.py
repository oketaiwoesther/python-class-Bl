# function is a block of code performing a specific task.
# syntax
# Declaring a function
# def function_name():
    # code
    # codes
# # Calling a function
# function_name()

def example_function():
    print('This is a function')
    example_function()

def add_numbers():
    num_one = 2
    num_two = 3
    total = num_one +num_two
    print(total)
add_numbers()
add_numbers()
add_numbers()
# class work
# A = PI*r**2 PI = 3.142
# when r = 3.5
def cal_area():
    r = 3.5
    Pi = 3.142
    A = Pi * r**2
    print(A)
cal_area()

def cal_area1(r, PI=3.142):
    A = PI * r**2
    print(A)
cal_area1(3.5)

def cal_area1(r, PI=3.142):
    A = PI * r**2
    print(int(A))
cal_area1(3.5)


def cal_area1(r, PI):
    A = PI * r**2
    print(int(A))
cal_area1(3.142,3.5)

## function with parameters
def full_name(first_name,last_name):
    print(f'My name is {first_name} {last_name}')
full_name('Blard', 'Omu')

def square_number(m):
    print(m**2)
square_number(9)


# 0+1 =1
# 1+2 =3
# 3+3 =6
# 6+4 =10
# 10+5 = 15
# 15+6 =21
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        # total = total + i
        total += i
    print(total)
sum_of_numbers(10)
print(sum_of_numbers(100))


# Arbitrary arguments, *arg
# siblings = ['kehinde','Taiwo','Idowu','dami','Abbey']
# def my_stack():
#     for name1 in siblings:
#         print(f'My name is {name1} ')
# my_stack()

# def my_siblings(*b):
#     print(f'The youngest child is {b[4]}')
#     print(f'The Techie child is {b[2]}')
#     print(f'The foodie child is {b[3]}')
# my_siblings('kehinde','Taiwo','Idowu','dami','Abbey')

# keyword arguments **arg
#key1 = value
# def myCal(l,b,h):
#     Vol = l*b*h
#     print(f'Volume is {Vol}cm^3 ')
# myCal(4,6,2)
# def myCal(l,b,h):
#     Vol = l*b-h
#     print(f'Volume is {Vol}cm^3 ')
# myCal(l=4,b=6,h=2)
# def myCal(**k):
#     print('This is ' + k['key3'])
#     print('This is ' + k['key1'])
#     print('This is ' + k['key2'])
#     print(f"'This is ' + {k['key2']}")
# myCal(key3='Taiwo',key2='praise',key1='kenny',key4='Oyin')

# def cal_vol(**y):
#     vol = y['key6']*y['key5']*y['key7']
#     print(vol)
# cal_vol(key5=2,key6=3,key7=4)

# def cal_vol(**y):
#     vol = y['key6']*y['key5']-y['key7']
#     print(vol)
# cal_vol(key5=2,key6=3,key7=4)

# def cal_vol(**y):
#     vol = y['key7']*y['key5']-y['key6']
#     print(vol)
# cal_vol(key5=2,key6=3,key7=4)

## Return statement
def my_return(first, second):
    return f'My name is {first} {second}'
print(my_return('Blard','Omu'))

def do_sum(a,b):
    return a+b*a-b
print(do_sum(5,6))

# pass
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
# def even_num():     
#     for i in range(1,21):
#         if i %2 == 0:
#             print((i) )
# even_num()

def even_num(n):  
    evens = []
    for i in range(n+1):
     if i %2 == 0:
            if i == 0:
                continue
            evens.append(i)
    return evens
print(even_num(20))

# lambda Function
# lambda args : expression
mySum = lambda a : a**2
print(mySum(5))

Vol_clinder = lambda p, r,h: p*r**2*h
print(Vol_clinder(3.142,7,4))
   
    
