import random as r

random = r.randint(0,9)
count = 0

while True:
    try:
        guess = int(input('เดา:'))
    except ValueError:
        print('ERROR')
        continue
    count += 1

    if random == guess:
        print('Correct')
        break
    elif guess > random:
        print('Too big')
    elif guess < random:
        print('Too small')
print(f'You guessed {count} times')