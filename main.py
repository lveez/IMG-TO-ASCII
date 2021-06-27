from PIL import Image, ImageEnhance
import sys

# RGB -> greyscale using conversion 0.3R + 0.59G + 0.11B
# made for use with consolas -> 55% font width

ascii_character = [' ', '.', ',', ':', ';', '-', '=', '+', '7',
                   '2', '9', '8', 'c', 'u', 'o', 'h', '#', '%', 'Q', 'M', '@', ]

# converts a list of rgb typles to luminance, and then to an index
# in the ascii character list above


def rgb_list_to_luminance_index_list(rgb_list):
    index_list = []
    for pixel in rgb_list:
        luminance = 0.3 * pixel[0] + 0.59 * pixel[1] + 0.11 * pixel[2]
        luminance /= 255
        index = int(round(luminance / 0.05))
        if index > 20:
            index = 20
        if index < 0:
            index = 0
        index_list.append(index)
    return index_list


def main():
    # default values -- filename is mandatory
    name = None
    brightness = 1
    contrast = 1
    # get arguments
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-b':
            brightness = float(sys.argv[i + 1])
        if sys.argv[i] == '-c':
            contrast = float(sys.argv[i + 1])
        if sys.argv[i] == '-n':
            name = sys.argv[i + 1]
    img = Image.open(name).resize((64, 35))
    # apply contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    # convert pixels to luminance
    rgb_list = list(img.getdata())
    index_list = rgb_list_to_luminance_index_list(rgb_list)
    # apply brightness
    for i in range(len(index_list)):
        index_list[i] = int(index_list[i] * brightness)
        if index_list[i] > 20:
            index_list[i] = 20
        if index_list[i] < 0:
            index_list[i] = 0
    # print out final ascii drawing
    i = 1
    string = ""
    for pixel in index_list:
        if i == 65:
            print(string)
            string = ""
            i = 1
        string += ascii_character[pixel]
        i += 1


if __name__ == '__main__':
    main()
