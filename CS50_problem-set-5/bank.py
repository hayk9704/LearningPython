def main():
    greeting = input("How are you doing? ").lower().strip()
    x = value(greeting)
    print(f"$ {x}")


def value(greeting):
    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("h"):
        return 20
    else:
        return 0
    
if __name__ =="__main__":
    main()