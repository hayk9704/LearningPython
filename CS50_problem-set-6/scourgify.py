import csv
import sys
list = []
if len(sys.argv) < 3:
    sys.exit("too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("too many arguments")

elif sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file) # dictreader
            for row in reader:
                last, first = row["name"].split(",")
                list.append({"first": first, "last": last, "house": row['house']})

        with open(sys.argv[2], "w", newline = "") as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for i in list:
                writer.writerow(i)
    except FileNotFoundError:
            sys.exit(f"could not read {sys.argv[1]}")
else:
    sys.exit("first is not a csv file")