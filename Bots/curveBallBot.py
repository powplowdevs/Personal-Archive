import pyautogui

while True:
    try:
        loc = pyautogui.locateOnScreen("G:\My Drive\Programing\Personal scripts\Bots\_ball.png", grayscale = True ,confidence=0.5)
        if loc != None:
            pyautogui.moveTo((loc[0]+50,loc[1]+50))
    except KeyboardInterrupt:
        quit()