def main():
    shorten(input())
def shorten(x):
    for i in x:
        if i.lower() in "aeiou":
            x = x.replace(i, "")
    return x

if __name__ =="__main__":
    main()