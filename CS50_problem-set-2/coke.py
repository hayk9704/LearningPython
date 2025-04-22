price = 50
print(f"Amount Due: {price}")
while True:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 20:
        price = price - coin
        if price > 0:
            print(f"amount due: {price}")
        elif price <= 0:
            print(f"change owed: {-price}")
            break
        