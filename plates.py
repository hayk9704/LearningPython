def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) == 2:
        is_valid2(s)
    elif len(s) == 3:
        is_valid3(s)
    elif len(s) == 4:
        is_valid4(s)
    elif len(s) == 5:
        is_valid5(s)
    elif len(s) == 6:
        is_valid6(s)

def is_valid2(s):
    for i in s:
        if i.isdigit():
            return False
        else:
            return True
def is_valid3(s):
    for i in s[0:1]:
        if i.isdigit:
            return False
def is_valid4(s):

def is_valid5(s):
def is_valid6(s):
main()