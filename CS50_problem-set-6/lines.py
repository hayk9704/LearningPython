import sys
code_num = 0
if len(sys.argv) > 2:
    sys.exit("too many command line arguments")
elif len(sys.argv) <2:
    sys.exit("too few command line arguments")
elif sys.argv[1].endswith(".py") is False:
    print("not a python file")
else:
    try:
        with open(sys.argv[1]) as file:
            for row in file:
                if row.lstrip() == "":
                    continue
                elif row.lstrip().startswith("#"):
                    continue
                else:
                    code_num = code_num + 1
        print(code_num)
    except FileNotFoundError:
        sys.exit("File does not exist")
