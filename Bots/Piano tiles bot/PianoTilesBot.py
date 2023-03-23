from PIL import ImageGrab
import pyautogui as pa
import time


# time.sleep(1)
# pa.moveTo(550,300)
# time.sleep(1)
# pa.moveTo(650,300)
# time.sleep(1)
# pa.moveTo(750,300)
# time.sleep(1)
# pa.moveTo(900,300)  


#home laptopp
#xs = (200,700)
#ys = (250,600) 
#school pc
xs =(500,930)
ys = (250,570)


      
time.sleep(1)   
image = ImageGrab.grab()
print("start")
while True:
    pa.press("space")
    #image = ImageGrab.grab()
    for y in range(ys[0], ys[1],50):
        image = ImageGrab.grab()   
        for x in range(xs[0], xs[1],50):
            color = image.getpixel((x, y))
            if color == (0,0,0):
                pa.moveTo(x,y+50)
                pa.click()
                #time.sleep(0.05)
                break
        
