deltax=0
deltay=0

def setup():
    size(1280, 720)
    
def draw():
    background(-1)
    mousepressfn()
    translate(width/2+deltax, height/2+deltay)
    ellipse(0, 0, 10, 10)
    
def mousepressfn():
    if mousePressed:
        dx = mouseX-pmouseX
        dy = mouseY-pmouseY
    else:
        dx = 0
        dy = 0
    global deltax
    global deltay
    deltax += dx
    deltay += dy
