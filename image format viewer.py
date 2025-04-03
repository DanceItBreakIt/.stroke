from PIL import Image

pixelr = 0
pixelg = 0
pixelb = 0

def getpixel(l, w):
    global pixelr
    global pixelg
    global pixelb
    pixelr = 0
    pixelg = 0
    pixelb = 0
    match image[index]:
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
            pixelr = 255 # purple
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
            pixelr = 200 # shades of yellow
            pixelg = 200
        case "U":
            pixelr = 100
            pixelg = 100
        case "V":
            pixelr = 55
            pixelg = 55

inputfile = input("paste the path to your binary file here: ")

with open(inputfile, mode='rb') as img: # b is important -> binary
    binarydata = img.read()
    image = binarydata.decode('utf-8')
    print(image[:12] + " - assuming good file, stroke image file \n\"stroke yourself silly!\"")

    if image[:12] == ")8GV!strokeL":
        length = ""
        width = ""
        index = 0

        for i in range(len(image)):
            if i > 11 and image[i] == "W":
                index = i
                print("length: " + length) # debug
                break
            elif i > 11:
                length = length + image[i]
        for i in range(len(image)):
            if i > index and image[i] == "G":
                index = i + 1
                print("width: " + width) # debug
                break
            elif i > index:
                width = width + image[i]

        print(image[index:]) # debug
        index += 1
        display = Image.new('RGB', (length, width))
        pixels = display.load()

        for i in range(len(image[index:])):
            for l in range(length):
                for w in range(width):
                    # return function here
                    pixels[l, w] = (pixelr, pixelg, pixelb)
                    index += 1
    else:
        pass