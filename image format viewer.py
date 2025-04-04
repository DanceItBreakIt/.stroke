from PIL import Image

pixelr = 0
pixelg = 0
pixelb = 0
index = 0

def getpixel(l, w):
    global pixelr
    global pixelg
    global pixelb
    pixelr = 0
    pixelg = 0
    pixelb = 0
    try:
        match image[index + ((w - 1) + (l + 0) * width)]: # cool pattern if you do image[index + w * l]
            case "A":
                pixelr = 255 # red
            case "B":
                pixelg = 255 # green
            case "C":
                pixelb = 255 # blue
            case "D":
                pixelr = 255 # yellow
                pixelg = 255
            case "E":
                pixelr = 255 # purple/magenta
                pixelb = 255
            case "F":
                pixelg = 255 # light blue
                pixelb = 255
            case "G":
                pixelr = 255 # white
                pixelg = 255
                pixelb = 255
            case "H":
                pixelr = 200 # shades of red
            case "I":
                pixelr = 100
            case "J":
                pixelr = 55
            case "K":
                pixelg = 200 # shades of green
            case "L":
                pixelg = 100
            case "M":
                pixelg = 55
            case "N":
                pixelb = 200 # shades of blue
            case "O":
                pixelb = 100
            case "P":
                pixelb = 55
            case "Q":
                pixelr = 200 # shades of yellow
                pixelg = 200
            case "R":
                pixelr = 100
                pixelg = 100
            case "S":
                pixelr = 55
                pixelg = 55
            case "T":
                pixelr = 200 # shades of purple/magenta
                pixelb = 200
            case "U":
                pixelr = 100
                pixelb = 100
            case "V":
                pixelr = 55
                pixelb = 55
            case "W":
                pixelg = 200 # shades of light blue
                pixelb = 200
            case "X":
                pixelg = 100
                pixelb = 100
            case "Y":
                pixelg = 55
                pixelb = 55
            case "Z": # black
                pass
            case "0":
                pixelr = 200 # shades of grey
                pixelg = 200
                pixelb = 200
            case "1":
                pixelr = 100
                pixelg = 100
                pixelb = 100
            case "2":
                pixelr = 55
                pixelg = 55
                pixelb = 55
            case "3":
                pixelr = 125
                pixelg = 125
                pixelb = 125
            case "4":
                pixelr = 150
                pixelg = 150
                pixelb = 150
            case "5":
                pixelr = 175
                pixelg = 175
                pixelb = 175
            case "6":
                pixelr = 225
                pixelg = 225
                pixelb = 225
            case "7":
                pixelr = 75
                pixelg = 75
                pixelb = 75
            case "8":
                pixelr = 25
                pixelg = 25
                pixelb = 25
            case "9":
                pixelr = 110 # brown
                pixelg = 60
            case _:
                pixelr = 255 # red
    except IndexError:
        pass

try:
    inputfile = input("paste the path to your binary file here: ")
except EOFError:
    inputfile = "/home/bounceandplounceonthatmouse/.stroke/new image format.stroke"
headerstring = ":)strokeL"

with open(inputfile, mode='rb') as img: # b is important -> binary
    binarydata = img.read()
    global image
    image = binarydata.decode('utf-8')
    print("\n" + image[:9] + " - reading stroke image file \n\"stroke yourself silly!\"")

    if image[:9] == headerstring:
        length = ""
        width = ""

        for i in range(len(image)):
            if i > 8 and image[i] == "W":
                index = i
                break
            elif i > 8:
                length = length + image[i]
        for i in range(len(image)):
            if i > index and image[i] == "!":
                index = i + 1
                break
            elif i > index:
                width = width + image[i]

        print("length: " + length) # debug
        print("width: " + width) # debug
        length = int(length)
        width = int(width)
        print(image[index:]) # debug
        index += 1
        display = Image.new("RGB", (length, width), (0,0,0))
        pixels = display.load()

        for i in range(len(image[index:])):
            for l in range(length):
                for w in range(width):
                    getpixel(l, w)
                    print(pixelr + pixelg + pixelb)
                    pixels[l, w] = (pixelr, pixelg, pixelb)
        display.save('/home/bounceandplounceonthatmouse/strokeimage.png')
    else:
        pass