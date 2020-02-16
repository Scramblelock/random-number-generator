from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!
import sys

# generate number range
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# check that input is a number within given range
while True:
    try:
        print(answer)
        # input from user
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if int(sys.argv[1]) <= guess <= int(sys.argv[2]):
            # check if number is the right guess, otherwise ask again
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print(f'hey bozo, I said {sys.argv[1]}~{sys.argv[2]}')
    except ValueError:
        print('please enter a number')
        continue







