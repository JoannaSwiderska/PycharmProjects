# we ask for input required data for the exercise
numbers = input('Provide 2 whole numbers for range where we seek fair and squre numbers (in following format: 1 4): ')

beginning = numbers.split(" ")[0]
ending = numbers.split(" ")[1]

# we validate provided data
while not beginning.isdigit() or int(beginning) == 0:
    print('You entered wrong data. First number needs to be whole number that is larger than 0')
    numbers = input(
        'Provide 2 whole numbers for range where we seek fair and squre numbers (in following format: 1 4): ')

while not ending.isdigit() or int(ending) == 0 or int(ending) < int(beginning):
    print('You entered wrong data. Second number needs to be whole number that is larger than first one')
    numbers = input(
        'Provide 2 whole numbers for range where we seek fair and squre numbers (in following format: 1 4): ')

fair_square = 0

for i in range(int(beginning), int(ending) + 1):
    # we make reversed number out of i
    i_reveresed = ''
    for num_digit in reversed(str(i)):
        i_reveresed += num_digit
    i_reveresed = int(i_reveresed)

    # we check if i is a square of whole number
    # if yes we make reversed number out of i_sqrt
    # otherwise we assume that reversed number to it is 0
    is_sqrt = False
    i_sqrt = i**(.5)
    if i_sqrt.is_integer():
        is_sqrt = True
        i_sqrt = int(i_sqrt)

        i_sqrt_reveresed = ''
        for num2_digit in reversed(str(i_sqrt)):
            i_sqrt_reveresed += num2_digit
        i_sqrt_reveresed = int(i_sqrt_reveresed)
    else:
        i_sqrt_reveresed = 0

    # we check if both numbers are palindromes
    if i_reveresed == i and i_sqrt_reveresed == i_sqrt:
        fair_square += 1


print(f'beginning: {beginning}, ending: {ending}')
print(f'fair and square count: {fair_square}')
