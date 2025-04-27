import sys
from tabulate import tabulate
import csv

if len(sys.argv) != 2:
    sys.exit("wrong number of command line arguments")
elif sys.argv[1].endswith(".csv") is False:
    sys.exit("not a CSV fileTABULATE_INSTALL=lib-only")
else:
    try: 
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers = "keys", tablefmt="heavy_grid"))
    except FileNotFoundError:
                sys.exit("file does not exist.")
