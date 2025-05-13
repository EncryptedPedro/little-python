#bot to beat the Sequence Memory Test by humanbenchmark.com

import pyautogui
from time import sleep

#the following coordinates are for my window positioning, you'll have to find your coordinates using pyautogui.position()
y1 = 400
y2 = 580
y3 = 740

x1 = 800
x2 = 950
x3 = 1100

coords = {
    "Square 1" : (x1, y1),
    "Square 2" : (x2, y1),
    "Square 3" : (x3, y1),
    "Square 4" : (x1, y2),
    "Square 5" : (x2, y2),
    "Square 6" : (x3, y2),
    "Square 7" : (x1, y3),
    "Square 8" : (x2, y3),
    "Square 9" : (x3, y3)
}

white = (255,255,255)
level=1

def scan(coords, sequence, level):
    for square, (x,y) in coords.items():
        if (pyautogui.pixel(x,y) == white):
            sequence.append(square)
            print("Found white at", square)
            sleep(0.5) #500ms wait before benchmark provides next square
            print(f"level {level}, step {len(sequence)}")
            if level==len(sequence):
                return True
    return False

def click(coords, sequence, level):
    countClick = 0
    while countClick < level:
        for seqSquare in sequence:
            for square, (x,y) in coords.items():
                if (square == seqSquare):
                    sleep(0.01)
                    pyautogui.click(x=x, y=y)
                    countClick = countClick+1
    return True #breaks out of loop if finished clicking

while (level<31):
    sequence = []
    scanning = True
    while (scanning):
        if scan(coords, sequence, level):
            scanning = False
    sleep(0.2)
    clicking = True
    while (clicking):
        if click(coords, sequence, level):
            clicking = False
    print(f"Completed level {level}: {sequence}")
    level += 1