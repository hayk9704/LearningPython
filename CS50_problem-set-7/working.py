import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^((?:[1-9]|1[0-2])(?::(?:0[0-9]|[1-5][0-9]))? (?:AM|PM)) to ((?:[1-9]|1[0-2])(?::(?:0[0-9]|[1-5][0-9]))? (?:AM|PM))$", s)
    if matches:
        if matches.group(1).endswith("AM"):
            first = convert_AM(matches.group(1))
        if matches.group(1).endswith("PM"):
            first = convert_PM(matches.group(1))
        if matches.group(2).endswith("AM"):
            second = convert_AM(matches.group(2))
        if matches.group(2).endswith("PM"):
            second = convert_PM(matches.group(2))
        return f"{first} to {second}"
    else:
        raise ValueError

def convert_AM(x):
    x = x.strip(" AM")
    if ":" in x:
        hour, minutes = x.split(":")
    else:
        hour = x
        minutes = "00"
    if hour == "12":
        hour = "00"
    else:
        hour = f"{int(hour):02}"
    return f"{hour}:{minutes}"

def convert_PM(x):
    x = x.strip(" PM")
    if ":" in x:
        hour, minutes = x.split(":")
    else:
        hour = x
        minutes = "00"
    if not hour == "12":
        hour = f"{int(hour) + 12:02}"
    return f"{hour}:{minutes}"


if __name__ == "__main__":
    main()