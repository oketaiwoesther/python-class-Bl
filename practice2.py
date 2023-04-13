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
'''accending order'''
scores.sort()
print(scores)

#decending order
scores.sort(reverse=True)
print(scores)

#maximum 
max_num = max(scores)
print(max_num)

#minimum
min_num = min(scores)
print(min_num)
print(len(scores))
mid_num = len(scores)/2
print(mid_num)
mid_num = len(scores)//2
print(mid_num)
median_num = print(scores[mid_num])

my_stack = front_end + back_end
print(my_stack)

add_stack = ['Python', 'SQL']
full_stack = front_end + add_stack + back_end
print(full_stack)
my_stack.extend(add_stack)
print(my_stack)
print(scores.count(24))

# add_stacks = ['Python', 'SQL']
# All_stack = front_end + add_stacks +back_end
# print(All_stack)  
  
# my_stacks.insert(5,'python')
# print(my_stacks)

# add_stacks = my_stacks.index('Redux')
# my_stacks.insert(add_stacks +1,'Python')
# my_stacks.insert(add_stacks +2,'SQL')
# print(my_stacks)

# Tuple 
# Tuple are collection of data type in python are another version of list they are declared in a parentheses ()
# Tuple is one of the four collection/sequence data type in python, tuple you have to convert it to list and use and then convert it back
#Tuple or tuple constructor function Tuple, tuple allow duplication.
tpl1 = tuple(())
print(tpl1)
tpl = ('string', -3,True)
print(tpl, type(tpl))
tpl1 = tuple((2, 'baby', 2))
print(tpl1,type(tpl1))
#accessing tuple
print(tpl1[1])

# len
print(len(tpl1))

# Udating tuples, tuples is in editable
# tpl1.append('sth')
tpl1_lst = list(tpl1)
print(tpl1_lst)

tpl1_lst[0] = 'item1'
print(tpl1_lst)
tpl1_lst.insert(1,'item1')
print(tpl1_lst)
print(tpl1_lst), type(tpl1_lst)

#change back to tuple
tpl1_lst = tuple(tpl1_lst)
print(tpl1_lst, type(tpl1_lst))
# del tpl1_lst

# slicing
team = ('LVP','PSG','ARS','CHE','MAN')
print(team[1::3])
print(team[:3])


# SETS
# set is also a collection of data type but it's element are enclosed in a curly braces {} set is unordered, set does not duplicate that is not having two numbers or variable in two.
# my_set = set({})
# print(my_set)
# print(type(my_set))
my_set1 = {'head', 7,'habit', False, 'Oyin'}
print(len(my_set1))
print(my_set1)

my_set2 = {'blue','yellow','green', 'red', 'black'}
print ('green'in my_set2)

import re

txt = "I Iove Techstudio and Python"
# match_it = re.match('I Iove' ,txt)
# match_it = re.match('Techstudio' ,txt[7:])
match_it = re.match('studio' ,txt[7:])
print(match_it)




