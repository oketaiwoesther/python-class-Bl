# Assignment
#build a simple calculator
import re
previous = 0
run = True

def my_cal():
    global previous
    global run
    do_math = " "
    # print('our calculator app running...')
    if previous == 0:
        do_math =input('Enter an expression: ')
    else:
        do_math =input(str(previous))
    if do_math == 'quit':
        print('Quit calculator app')
        run = False
    else:
        do_math = re.sub('[a-zA-Z,.:()""]','',do_math)
        if previous == 0:
            previous = eval(do_math)
        else:
            previous = eval(str(previous)+do_math)
while run:
    my_cal()
# greatfronted.com



