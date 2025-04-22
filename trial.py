x = input("")
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    for i in plate:
        if i.isalpha():
            return True
        else:
            return False
        
main()