import random


def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        correct = 0
        while True:
            try:
                z = int(input(f"{x} + {y} = "))
                if z == x + y:
                    score = score + 1
                    break
                else:
                    print("EEE")
                    correct = correct + 1
                    if correct < 3:
                        continue
                    else:
                        print(f"{x} + {y} = {x + y}")
                        break
            except ValueError:
                print("EEE")
                correct = correct + 1
                if correct < 3:
                    continue
                else:
                    print(f"{x} + {y} = {x + y}")
                    break
    print(f"Score: {score}")
def get_level():
    while True:
        try:
            n = int(input("level: "))
            if  n <1 or n >3:
                continue
            else:
                break
        except ValueError:
            continue
    return n


def generate_integer(level):
    if level == 1:
        x = random.randint(1,9)
        return x
    if level == 2:
        x = random.randint(10,99)
        return x
    if level == 3:
        x = random.randint(100, 999)
        return x
    else:
        raise ValueError

    


if __name__ == "__main__":
    main()