import pyautogui
from PIL import Image, ImageGrab
import time
def hit(key): #function to automate keyboard
    pyautogui.press(key)
    return
def isCollide(data): #function to check for cactus and birds 
    #check for birds
    for i in range(210,250):
        for j in range(300,380):
            if data[i,j] < 100:
                hit("down") #if a bird is detected ahead of dino down key is pressed
    #check for cactus
    for i in range(220,330):
        for j in range(455,500):
            if data[i,j] < 100:  #0 means black and 255 means white
                hit("up") ##if a cactus is detected ahead of dino up key is pressed
                return 
    return 

if __name__=='__main__':
    print("Hey Dino game is about to start in 2 seconds")
    time.sleep(2) # wait for 2 seconds
    hit("up") # start the dino game
    while True:
        image = ImageGrab.grab().convert('L')  # takes ss and converts image to greyscale
        
        data = image.load()
        isCollide(data)

        #documentation to set the space to detect cactus and birds
        #set it according to screen resolution by hit and trail method
    '''
        #draw the rectangle for cactus
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
    
    
    
    





