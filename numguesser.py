import helpers

print('Enter the LOWER bounds of your range:')
lower = input()
lower = helpers.integer_check(lower)

print('Enter the UPPER bounds of your range:')
upper = input()
upper = helpers.integer_check(upper)

range = helpers.validate_range([lower, upper])

print('\nPick a number within your range and remember it,')
print('I will arrive at your number in less than {max} guesses\n'.format(
    max = helpers.get_max_guesses(range)))

left, right = range[0], range[1]
numGuesses = 0

while left <= right:
    numGuesses += 1
    mid = (left + right) // 2
    print("Is your number 'greater' than, 'less' than, or 'equal' to {guess}".format(guess = mid))
    side = input()
    sideVal = helpers.gle_input_check(side, mid)

    if sideVal == 0:
        break
    elif sideVal == 1:
        left = mid + 1
    else:
        right = mid - 1

print('\n----------------------')
print("Your number was {n}, it took {g} guesses to get there.".format(n = mid, g = numGuesses))
print('----------------------\n')
print('Thanks for playing\n')
