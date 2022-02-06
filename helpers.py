import math

#make sure user entered an integer
def integer_check(bound):
    while 1:
        try:
            bound = int(bound)
            break

        except ValueError:
            print('Invalid Input, Integers Only - Try Again:')
            bound = input()
    
    return bound

#ensure lower bounds is lower than upper
def validate_range(range):
    l = min(range)
    u = max(range)

    return [l,u]

#returns max guesses computer will need to arrive at users numeber
def get_max_guesses(rangeList):
    rangeVal = rangeList[1] - rangeList[0]
    num = math.log(rangeVal, 2)

    return math.ceil(num)
    
def gle_input_check(side, guess):
    while 1:
        side = side.lower()
        if side == 'less':
            return -1
        elif side == 'greater':
            return 1
        elif side == 'equal':
            return 0

        else:
            print("Invalid Input, please enter decide if your number is 'greater', 'less', or 'equal' to {g}".format(g = guess))
            side = input()