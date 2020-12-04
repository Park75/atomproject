value = 0

def setup():
    size(640, 360)
    noStroke()
    fill(0)

def draw():
    background(204)
    #if (keyPressed):   # If the key is pressed,
        #line(20, 20, 80, 80)   # draw a line
    #else:   # Otherwise,
        #rect(40, 40, 20, 20)   # draw a rectangle
        

    if((mouseX>40) and (mouseX<80) and (mouseY>20) and (mouseY<80)):
        fill(123)
    else:
        fill(0) #Hier Beschriftung von Atom
    rect(40,20,40,60)
    
    if((mouseX>100) and (mouseX<140) and (mouseY>20) and (mouseY<80)):
        fill(123)
    else:
        fill(0) #Hier Beschriftung von Atom
    rect(100,20,40,60)
    

    fill(value)    
    rect(40, 100, 50, 50)
        
def mouseClicked():
    global value
    if value == 0:
        value = 255
    else:
        value = 0
        
    fill(value)    
    rect(100, 100, 50, 50)
        
def mouseClicked():
    global value
    if value == 0:
        value = 255
    else:
        value = 0



    
