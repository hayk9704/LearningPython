import random
while True:
    try:
        n = input("Level: ")
        if int(n) < 1:
            continue
        else:
            break
    except ValueError:
        continue
num = random.randint(1,int(n))
while True:
    try:
        guess = input("Guess: ")
        if int(guess) < num:
            print("Too small")
        elif int(guess) > num:
            print("Too large")
        else:
            print("Just right")
            break
    except ValueError:
        continue