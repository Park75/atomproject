totalFrames = 120;
counter = 0.0

def setup():
    size(800, 500)
    strokeWeight(2)
    
    
def draw():
    global counter
    
    background(255)
    percent = counter / totalFrames
    atomCore()
    drawLines()
    render(percent)    
    
    counter = counter + 1

def atomCore():
    fill(0, 0, 0)
    circle(400, 250, 50)
    
def drawLines():
    noFill()
    circle(400, 250, 145)

def render(percent):
    angle = percent * TWO_PI;
    translate(width/2, height/2)
    fill(255, 0, 0)
    rotate(angle)
    circle(50, 50, 20)
    
