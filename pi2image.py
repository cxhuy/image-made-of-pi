from PIL import Image

width = 1000
size = 10

digits = open("pi.txt", 'r')
blank = Image.new('RGB', (width, width), color='white')

num = 0
r, g, b = 0, 3, 6

line = digits.readline()

def rgb(x):
    return line[x] + line[x + 1] + line[x + 2]

def paint(rgb, num):
    pix = Image.new('RGB', (size, size), color=(rgb[0], rgb[1], rgb[2]))
    blank.paste(pix, (int(num % (width / size)) * size, int(num / (width / size)) * size))

while num < pow((width / size), 2):
    red = int(rgb(r))%256
    green = int(rgb(g))%256
    blue = int(rgb(b))%256

    paint((red, green, blue), num)
    
    num += 1
    r += 9
    g += 9
    b += 9

blank.save('result.png')
digits.close()
