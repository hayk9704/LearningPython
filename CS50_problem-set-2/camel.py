camel = input("camelCase: ")
for i in camel:
    if i.capitalize() == i:
        print(f"_{i.lower()}", end = "")
    else:
        print(i, end = "")
