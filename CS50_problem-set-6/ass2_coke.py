x = 50

# hello
while x >=0:
    y = int(input("Insert Coin: "))
    if y ==5 or y==10 or y==15 or y==25:
        x = int(x)-int(y)
        if x <= 0:
            print("change owed:", int(-x))
            break
        else:
            print("amount due:", int(x))
    else:
        print("amount due:", int(x))