from time import sleep
import pyautogui

print(pyautogui.pixel(216,399))

blue = (43,135,209)
green = (75,219,106)
print(green)

while True:
    if (pyautogui.pixel(216,399) == green):
        #sleep(0.08)
        pyautogui.click()
        break