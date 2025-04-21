def main():
    time = convert(input("what time is it? "))
    if 8<= time <= 9:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    minute = float(minute)/60
    hour = float(hour.removeprefix("0"))
    newtime = minute + hour
    return newtime

if __name__ == "__main__":
    main()