def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif len(s) == 2 and s[0:1].isalpha():
         return True
    elif len(s) == 3:
         if s[0:1].isalpha() and s[2] != "0":
              return True
         else:
              return False
    elif len(s) > 3:
        if s[0:1].isalpha() is False:
            return False
        elif any(s[i].isdigit() and s[i+1].isalpha() for i in range(2,len(s)-1)):
                return False
        elif any(s[i].isalpha() and s[i+1] == "0" for i in range(1,len(s)-1)):
                return False
        else:
             return True
    
        
main()