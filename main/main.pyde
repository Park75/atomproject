import Atom;

# Anzahl Frames beeinflusst die Geschwindigkeit der Elektronen
totalFrames = 180;
# counter zählt wie oft die Methode draw() aufgerufen wurde.
counter = 0.0;
li = Atom;
mg = Atom;
al = Atom;

def setup():
    size(1500, 700);             # Fenstergrösse
    strokeWeight(2);             # Stärke der Linie
    
    # Erstellen des Atomes mg mit den Angaben, wie viel Elektronen sich auf den einzelnen Schalen befinden.
    global li;
    global mg;
    global al;
    li = Atom.Atom(2, 2, 1, 0);  
    mg = Atom.Atom(3, 2, 8, 2);  
    al = Atom.Atom(3, 2, 8, 3);  
    
    
def draw():
    global counter;
    translate(400, 250);       # Legt Nullkoordinate fest, könnte auch auf die Breite oder Länge des Fensters fokussiert werden
    background(255);
    
    percent = counter / totalFrames;
    atomCore();
    drawLinesAtomShells();
    render(percent);      
    
    counter = counter + 1;

# Atomkern wird gezeichnet
def atomCore():
    fill(0, 0, 0);
    circle(0, 0, 50);
    
# einzelne Schalen des Atommodells werden gezeichnet 
def drawLinesAtomShells():
    noFill();
    circle(0, 0, 150);
    circle(0, 0, 250);    
    circle(0, 0, 350);

# Zeichnen der einzelnen Elektronen, bei jedem erneuten Aufruf werden die Elektronen um den berechneten Winkel verschoben
def render(percent):
    global mg;
    angle = percent * HALF_PI;
    
    rotate(angle);                                             # Umdrehung um den angegebenen Winkel in Rad    
    
     
    # Abrufen und festhalten in der Liste electronCoordinates der Koordinaten für die darzustellende Elektornen
    electronCoordinates = mg.getAllElectronCoordinate();
    
    # Zeichnen jedes einzelnen Elektrons um es darzustellen
    for current_Electron in range(0, len(electronCoordinates)):
        fill(255, 0, 0);                                           # Farbe Rot
        circle(electronCoordinates[current_Electron][0], electronCoordinates[current_Electron][1], 20);
        fill(0, 0, 0);                                           # Farbe schwarz
        rect(electronCoordinates[current_Electron][0]-5, electronCoordinates[current_Electron][1], 10, 1);
        
   


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
