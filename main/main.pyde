import Atom;

# Anzahl Frames beeinflusst die Geschwindigkeit der Elektronen
totalFrames = 180;
# counter zählt wie oft die Methode draw() aufgerufen wurde.
counter = 0.0;
li = Atom;
mg = Atom;
al = Atom;
totalFrames = 180;
electronCoordinates = [];

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
    
    noStroke()
    fill(0)
    textSize(20)
    font = createFont("Corbel",30)
    textFont(font)
    
    
def draw():
    global counter;
    translate(400, 250);       # Legt Nullkoordinate fest, könnte auch auf die Breite oder Länge des Fensters fokussiert werden
    background(255);
    
    control();
    
    percent = counter / totalFrames;
    atomCore();
    drawLinesAtomShells();
    render(percent);      
    
    counter = counter + 1;

# Atomkern wird gezeichnet
def atomCore():
    fill(0, 0, 0)
    stroke(255)
    circle(-15, 0, 30)
    circle(0, 15, 30)
    circle(15, 0, 30)
    circle(0, -15, 30)
    circle(0, 0, 30)
    stroke(0)
    
# einzelne Schalen des Atommodells werden gezeichnet 
def drawLinesAtomShells():
    noFill();
    circle(0, 0, 150);
    circle(0, 0, 250);    
    circle(0, 0, 350);

# Zeichnen der einzelnen Elektronen, bei jedem erneuten Aufruf werden die Elektronen um den berechneten Winkel verschoben
def render(percent):
    global electronCoordinates;
    angle = percent * HALF_PI;
    
    rotate(angle);                                             # Umdrehung um den angegebenen Winkel in Rad    
    
     
    # Abrufen und festhalten in der Liste electronCoordinates der Koordinaten für die darzustellende Elektornen
    #electronCoordinates = mg.getAllElectronCoordinate();
    
    # Zeichnen jedes einzelnen Elektrons um es darzustellen
    for current_Electron in range(0, len(electronCoordinates)):
        fill(255, 0, 0);                                           # Farbe Rot
        circle(electronCoordinates[current_Electron][0], electronCoordinates[current_Electron][1], 20);
        fill(0, 0, 0);                                           # Farbe schwarz
        rect(electronCoordinates[current_Electron][0]-5, electronCoordinates[current_Electron][1], 10, 1);
        
   



#Lithium =rect(20,40,20,20)
#Magnesium =rect(20,80,20,20)
#Aluminium =rect(20,120,20,20)

def control():
    global electronCoordinates;
    # Steuerung / Auswahl Li, Mg, Al
    rect(20,40,20,20)
    rect(20,80,20,20)
    rect(20,120,20,20)
    text ("Lithium", 50,60)
    text ("Magnesium", 50,100)
    text ("Aluminium", 50,140)

#Lithium    
    if((mouseX>420) and (mouseX<440) and (mouseY>290) and (mouseY<310) and mousePressed):
        electronCoordinates = [];
        electronCoordinates = li.getAllElectronCoordinate();
        fill (255)
        rect(20,40,20,20)    
    else:
        print ("False")
        
    if ((keyPressed) and ((key == "L") or (key == "l"))):
        electronCoordinates = [];
        electronCoordinates = li.getAllElectronCoordinate();
        fill (255)
        rect(20,40,20,20)
    else:
        print ("False")
        
#Magnesium        
    if((mouseX>20) and (mouseX<40) and (mouseY>80) and (mouseY<100)and mousePressed):
        electronCoordinates = [];
        electronCoordinates = mg.getAllElectronCoordinate();
        fill (255)
        rect(20,80,20,20)
    else:
        print ("False")
        
    if ((keyPressed) and ((key == "M") or (key == "m"))):
        electronCoordinates = [];
        electronCoordinates = mg.getAllElectronCoordinate();
        fill (255)
        rect(20,80,20,20)
    else:
        print ("False")
        
#Aluminium
    if((mouseX>20) and (mouseX<40) and (mouseY>120) and (mouseY<140)and mousePressed):
        electronCoordinates = [];
        electronCoordinates = al.getAllElectronCoordinate();
        fill (255)
        rect(20,120,20,20)
    else:
        print ("False")
        
    if ((keyPressed) and ((key == "A") or (key == "a"))):
        electronCoordinates = [];
        electronCoordinates = al.getAllElectronCoordinate();
        fill (255)
        rect(20,120,20,20)
    else:
        print ("False")
        
