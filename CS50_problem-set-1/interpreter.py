exp = input("Expression: ")
x, y, z = exp.split(" ")
if y == "+":
    m = int(x) + int(z)
    print(f"{m:.1f}")
elif y == "-":
    m = int(x) - int(z)
    print(f"{m:.1f}")
elif y == "*":
    m = int(x)*int(z)
    print(f"{m:.1f}")
elif y == "/":
    m = int(x)/int(z)
    print(f"{m:.1f}")
elif y == "/" and z == 0:
    print("undefined")