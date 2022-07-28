from drawingpanel import *
import sys

# python speed_reader.py example.txt 400 200 18 350
def modString(t):

    num = 0
    addedSpaces = 0
    coloredText = ""
    if len(t) == 1:
        coloredText = t[0]
        return [t, coloredText]
    if len(t) == 2:
        t = t + ' '
        coloredText = t[1]
        return [t, coloredText]
    elif len(t) == 3:
        coloredText = t[1]
        return [t, coloredText]
    elif len(t) == 4:
        t = ' ' + t
        coloredText = t.strip()[1]
        return [t, coloredText]
    elif len(t) == 5:
        t = ' ' + ' ' + t
        coloredText = t.strip()[1]
        return [t, coloredText]

    if len(t) >= 6 and len(t) <= 9:
        addedSpaces = 1
        num = 6
    if len(t) >= 10 and len(t) <= 13:
        addedSpaces = 3
        num = 10
    if len(t) > 13:
        num = 13
        addedSpaces = 4

    for i in range(0, len(t) - num):
        t = ' ' + t
    t = (addedSpaces * ' ') + t
    if num == 6:
        coloredText = t.strip()[2]
    elif num == 10:
        coloredText = t.strip()[3]
    elif num == 13:
        coloredText = t.strip()[4]

    return [t, coloredText]

def animate_text(panel, filename, width, height, font_size, wpm):
    delay = 60000 / wpm
    count = 0
    newStr = ""
    canvas = panel.canvas

    f = open(filename, 'r')
    lst_of_words = f.readlines()
    for i in range(0, len(lst_of_words)):
        lst_of_words[i] = lst_of_words[i].replace("\n", "")
        newStr += lst_of_words[i] + " "
    newStr = newStr.strip()

    lst_of_words = newStr.split(" ")

    while count < len(lst_of_words):
        coloredText = ""
        print("word: ", lst_of_words[count])
        t = lst_of_words[count]
        timesTwo = False

        if len(t) > 0:
            timesTwo = t[-1] == ';' or t[-1] == '.' or t[-1] == ','


        stuff = ["", ""]
        if len(t) > 0:
            stuff = modString(t)



        canvas.create_text(width / 2, height / 2, text = stuff[0], font = ("Courier", str(font_size), 'bold'))
        canvas.create_text(width / 2, height / 2, text = stuff[1], font = ("Courier", str(font_size), 'bold'), fill = "red")

        if(timesTwo):
            panel.sleep(delay*2)
        else:
            panel.sleep(delay)

        canvas.delete("all")

        count += 1

def main():
    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    size = int(sys.argv[4])
    wpm = int(sys.argv[5])


    panel = DrawingPanel(width, height)
    panel.set_background("white")

    animate_text(panel, filename, width, height, size, wpm)

if __name__ == '__main__':
    main()
