import datetime
import sys
import inflect
p = inflect.engine()
if len(sys.argv) == 2:
    try:
        x = datetime.date.today() - datetime.date.fromisoformat(sys.argv[1])
    except ValueError:
        sys.exit("Invalid Date")
else:
    sys.exit("Must be 1 argument")
    
minutes = int(x.days)*24*60
print(x.days)
min_words = p.number_to_words(minutes, andword="")
print(min_words, "minutes")
