def main():
    x = input("fraction: ")
    y = convert(x)
    gauge(y)


def convert(fraction):
    a, b = fraction.split("/")
    if int(b) == 0:
        raise ZeroDivisionError
    if int(a) > int(b):
        raise ValueError
    return round(int(a)/int(b)*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()