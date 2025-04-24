while True:
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
        if int(x) < 0 or int(y) < 0:
            continue
        if   0.99 <= int(x)/int(y) <=1:
            print("F")
            break
        elif 1<= int(x)/int(y) <= 0.01:
            print("E")
            break
        elif int(x)/int(y) < 1:
            print(f"{round(int(x)/int(y)*100)}%")
            break
        else:
            pass
    except ValueError or ZeroDivisionError:
        pass