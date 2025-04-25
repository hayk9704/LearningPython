list = {}
while True:
    try:
        x = input().upper().strip()
        if x in list:
            list[x] = list[x] + 1
        else:
            list[x] = 1
    except EOFError:
        for i in sorted(list):
            print(f"{list[i]} {i}")
        break