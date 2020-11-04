totalFrames = 120;
counter = 0.0;
numb_elektronen_shell1 = 2
numb_elektronen_shell2 = 8
numb_elektronen_shell3 = 2
numbShell = 3

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
    circle(0, 0, 150)
    circle(0, 0, 250)    
    circle(0, 0, 350)

def render(percent):
    global numbShell
    
    angle = percent * HALF_PI
    fill(255, 0, 0)                                           # Farbe Rot
    rotate(angle)                                             # Umdrehung um den angegebenen Winkel in Rad
    
    for current_shell in range(0, numbShell):
        if current_shell == 0:
            renderElectrons(numb_elektronen_shell1, getDefaultCoordinateX(), getDefaultCoordinateY_Shell1())
        if current_shell == 1:
            renderElectrons(numb_elektronen_shell2, getDefaultCoordinateX(), getDefaultCoordinateY_Shell2())
        if current_shell == 2:
            renderElectrons(numb_elektronen_shell3, getDefaultCoordinateX(), getDefaultCoordinateY_Shell3())
    

def renderElectrons(numb_elektronen_shell, defaultCoordinateX, defaultCoordinateY):
    for i in range(0, numb_elektronen_shell):
        if i == 1:
            defaultCoordinateY *= -1
        if i == 2:
            defaultCoordinateX = defaultCoordinateY
            defaultCoordinateY = 0
        if i == 3:
            defaultCoordinateX *= -1
              
        circle(defaultCoordinateX, defaultCoordinateY, 20)        # Kreis mit Grösse = 20
    
   

# 1. SChale 2
# 2. Schale 8
# 3. Schale 2

def getDefaultCoordinateX():
    return 0

def getDefaultCoordinateY_Shell1():
    return 75

def getDefaultCoordinateY_Shell2():
    return 125

def getDefaultCoordinateY_Shell3():
    return 175
