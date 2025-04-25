list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if "/" in date:
            m, d, y = date.split("/")
            if int(m) > 12 or int(d) > 31 or int(m) < 1 or int(d) < 1:
                continue
            d = f"{int(d):02d}"
            m = f"{int(m):02d}"
            print(f"{y}-{m}-{d}")
        elif "," in date:
            a, y = date.split(", ")
            m, d = a.split(" ")
            m = m.lower().capitalize()
            d = f"{int(d):02d}"
            if int(d) > 31 or int(d) < 1:
                    continue
            if m in list:
                m = list.index(m)
                m = f"{int(m+1):02d}"
                print(f"{y}-{m}-{d}")
                break
            else:
                continue
    except ValueError:
        continue
