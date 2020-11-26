import Atom;

totalFrames = 120;
counter = 0.0;
electronCoordinates = []


def setup():
    size(1500, 700)             # Fenstergrösse
    strokeWeight(2)             # Stärke der Linie
    
    
def draw():
    global counter
    translate(400, 250)       # Legt Nullkoordinate fest, könnte auch auf die Breite oder Länge des Fensters fokussiert werden
    background(255)
    
    percent = counter / totalFrames
    atomCore()
    drawLinesAtomShells()
    render(percent)      
    
    counter = counter + 1


def atomCore():
    fill(0, 0, 0)
    circle(0, 0, 50)
    
def drawLinesAtomShells():
    noFill()
    circle(0, 0, 150)
    circle(0, 0, 250)    
    circle(0, 0, 350)

def render(percent):
    angle = percent * HALF_PI
    fill(255, 0, 0)                                           # Farbe Rot
    rotate(angle)                                             # Umdrehung um den angegebenen Winkel in Rad    
    
    mg = Atom.Atom(3, 2, 8, 2);   
    electronCoordinates = mg.getAllElectronCoordinate();
       
    for current_Electron in range(0, len(electronCoordinates)):
        circle(electronCoordinates[current_Electron][0], electronCoordinates[current_Electron][1], 20)
   


def Buttons():

#Möglichkeit für Buttons

#1. Mouseposition
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
    
#2.Keypress (Einfachste Lösung)
    #if (keyPressed):   # If the key is pressed,
        #line(20, 20, 80, 80)   # draw a line
    #else:   # Otherwise,
        #rect(40, 40, 20, 20)   # draw a rectangle
        
#3.Mouseclicked (Kompliziert in Python)
 #fill(value)    
    #rect(40, 100, 50, 50)
        
#def mouseClicked():
    #global value
    #if value == 0:
        #value = 255
    #else:
        #value = 0
