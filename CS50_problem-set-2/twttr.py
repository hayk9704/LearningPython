x = input("Input: ")
for i in x:
    if i.lower() in "aeiou":
        x = x.replace(i, "")
print("Output: ", x)