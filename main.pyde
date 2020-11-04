totalFrames = 120;
counter = 0.0;

def setup():
    size(1500, 700)             # Fenstergrösse
    strokeWeight(2)             # Stärke der Linie
    
    
def draw():
    global counter
    translate(400, 250)       # Legt Nullkoordinate fest, könnte auch auf die Breite oder Länge des Fensters fokussiert werden
    background(255)
    
    percent = counter / totalFrames
    atomCore()
    drawLines()
    render(percent)      
    
    counter = counter + 1


def atomCore():
    fill(0, 0, 0)
    circle(0, 0, 50)
    
def drawLines():
    noFill()
    circle(0, 0, 145)

def render(percent):
    defaultCoordinateX = 0
    defaultCoordinateY = 70
    angle = percent * HALF_PI;
    fill(255, 0, 0)                                           # Farbe Rot
    rotate(angle)                                             # Umdrehung um den angegebenen Winkel in Rad
             
    for i in range(1, 3):
        if i%2==0:
            defaultCoordinateY *= -1                         
        circle(defaultCoordinateX, defaultCoordinateY, 20)        # Kreis mit Grösse = 20
    
