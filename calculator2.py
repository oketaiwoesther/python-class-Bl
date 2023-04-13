import re
run = True
previous = 0
def my_calc():
    global run
    global previous
    if previous == 0:
        expression = input('Enter expression ')
    else:
        expression = input(str(previous))
    # Control loop and evaluate
    if expression == "quit":
        print('Goodbye human!')
        run = False
    else:
        #regex
        if previous == 0:
            expression = re.sub('[a-zA-Z,.?();:@]', '',expression)
            previous = eval(expression)
        else:
            previous = eval(str(previous) + expression)
            print('Ans: ',previous)
            
while run:
    my_calc()
         
