def main():
    print(convert(input()))

def convert(x):
    x = x.replace(":)", "🙂" )
    return x.replace(":(", "🙁")
main()