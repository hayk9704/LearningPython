import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    amount = 0
    for i in re.findall(r"(\b[u|U][m|M]\b)", s):
        amount = amount + 1
    return amount



if __name__ == "__main__":
    main()