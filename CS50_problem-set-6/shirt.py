from PIL import Image, ImageOps
import sys
import os
formats = [".png", ".jpg", ".jpeg"]
shirt = Image.open("shirt.png")

if len(sys.argv) != 3:
    sys.exit("2 command line arguments needed")
elif not os.path.splitext(sys.argv[1])[1] in formats or not os.path.splitext(sys.argv[1])[1] in formats:
    sys.exit("incorrect extension")
elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("command line arguments do not match")


try:
    file = Image.open(sys.argv[1])
except FileNotFoundError:
     sys.exit("file not found")
newfile = ImageOps.fit(file, (600,600))
newfile.paste(shirt, shirt)
newfile.save(sys.argv[2])