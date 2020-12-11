import Atom;

# Anzahl Frames beeinflusst die Geschwindigkeit der Elektronen
totalFrames = 180;
# counter zählt wie oft die Methode draw() aufgerufen wurde.
counter = 0.0;
li = Atom;
mg = Atom;
al = Atom;
electronCoordinates = [];
nameAtom = "";
cordinateYWhiteRect = 0;


def setup():
    size(1500, 700);             # Fenstergrösse
    strokeWeight(2);             # Stärke der Linie
    fill(0)
    textSize(20)
    font = createFont("Corbel",30)
    textFont(font)
    
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
    
    control();
        
    atomCore();
    drawLinesAtomShells();
    
    # percent rechnet die prozentualle Verschiebung aus, aufgrund wie oft draw() bereits aufgerufen wurde. 
    percent = counter / totalFrames;
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

    # Zeichnen jedes einzelnen Elektrons um es darzustellen
    for current_Electron in range(0, len(electronCoordinates)):
        fill(255, 0, 0);                                           # Farbe Rot
        circle(electronCoordinates[current_Electron][0], electronCoordinates[current_Electron][1], 20);
        fill(0, 0, 0);                                             # Farbe schwarz
        rect(electronCoordinates[current_Electron][0] - 5, electronCoordinates[current_Electron][1], 10, 1);




def control():
    global electronCoordinates;
    global nameAtom;
    global cordinateYWhiteRect;
    
    # Anzeige der Navigation
    navigationBar();

#Lithium    
    if((mouseX>650) and (mouseX<670) and (mouseY>250) and (mouseY<270) and mousePressed):
        nameAtom = "Lithium";
        electronCoordinates = [];
        electronCoordinates = li.getAllElectronCoordinate();
        cordinateYWhiteRect = 0;
        # weisses Rechteck (zur Anzeige des aktuellen Atoms) wird überschrieben, damit es nicht mehr angezeigt wird.
        rectWhite = rect(0,0,0,0)   

    if ((keyPressed) and ((key == "L") or (key == "l"))):
        nameAtom = "Lithium";
        electronCoordinates = [];
        electronCoordinates = li.getAllElectronCoordinate();
        cordinateYWhiteRect = 0;
        # weisses Rechteck (zur Anzeige des aktuellen Atoms) wird überschrieben, damit es nicht mehr angezeigt wird.
        rectWhite = rect(0,0,0,0)
        
#Magnesium        
    if((mouseX>650) and (mouseX<670) and (mouseY>290) and (mouseY<310)and mousePressed):
        nameAtom = "Magnesium";
        electronCoordinates = [];
        electronCoordinates = mg.getAllElectronCoordinate();
        cordinateYWhiteRect = 40;
        # weisses Rechteck (zur Anzeige des aktuellen Atoms) wird überschrieben, damit es nicht mehr angezeigt wird.
        rectWhite = rect(0,0,0,0)
        
    if ((keyPressed) and ((key == "M") or (key == "m"))):
        nameAtom = "Magnesium";
        electronCoordinates = [];
        electronCoordinates = mg.getAllElectronCoordinate();
        fill (255)
        rect(250,40,20,20)
        cordinateYWhiteRect = 40;
        # weisses Rechteck (zur Anzeige des aktuellen Atoms) wird überschrieben, damit es nicht mehr angezeigt wird.
        rectWhite = rect(0,0,0,0)
        
#Aluminium
    if((mouseX>650) and (mouseX<670) and (mouseY>330) and (mouseY<350)and mousePressed):
        nameAtom = "Aluminium";
        electronCoordinates = [];
        electronCoordinates = al.getAllElectronCoordinate();
        cordinateYWhiteRect = 80
        # weisses Rechteck (zur Anzeige des aktuellen Atoms) überschrieben, damit es nicht mehr angezeigt wird.
        rectWhite = rect(0,0,0,0)
        
    if ((keyPressed) and ((key == "A") or (key == "a"))):
        nameAtom = "Aluminium";
        electronCoordinates = [];
        electronCoordinates = al.getAllElectronCoordinate();
        cordinateYWhiteRect = 80
        # weisses Rechteck (zur Anzeige des aktuellen Atoms) überschrieben, damit es nicht mehr angezeigt wird.
        rectWhite = rect(0,0,0,0)
        
    fill (255);
    rectWhite = rect(250,cordinateYWhiteRect,20,20);
      

# Anzeige der Navigation
def navigationBar():
    global nameAtom;
    global cordinateYWhiteRect;
    
    # Steuerung / Auswahl Li, Mg, Al
    rect(250, 0, 20, 20)
    rect(250, 40, 20, 20)
    rect(250, 80, 20, 20)
    text ("Lithium", 280, 20)
    text ("Magnesium", 280, 60)
    text ("Aluminium", 280, 100)
    fill(0)
    text(nameAtom, -50, -200)
