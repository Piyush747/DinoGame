import pyautogui
from PIL import Image, ImageGrab
import time
#from numpy import asarray
def hit(key):
    pyautogui.press(key)
    return
#def draw():
def isCollide(data):
    #check for birds
    for i in range(210,250):
        for j in range(300,380):
            if data[i,j] < 100:
                hit("down")
    #check for cactus
    for i in range(220,330):
        for j in range(455,500):
            if data[i,j] < 100:  #0 means black and 255 means white
                hit("up")
                return 
    return 

if __name__=='__main__':
    print("Hey Dino game is about to start in 3 seconds")
    time.sleep(2)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')  # takes ss and converts image to greyscale
        
        data = image.load()
        isCollide(data)
        #print(asarray(image))

        #draw the rectangle for cactus
        
    '''
        for i in range(220,300):
            for j in range(455,500):
                data[i,j]=0
        #draw the rectange for birds
        for i in range(210,250):
            for j in range(300,380):
                data[i,j]=0

        
                

        image.show()
        break
    '''
    
    
    
    





