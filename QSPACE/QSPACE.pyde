#Canvas params
deltax=0
deltay=0
bgcolour = color(200, 200, 200)
#Graphics params
pointr = 10
pointstroke = color(0, 0, 0)
pointfill = color(255, 255, 255)
#Model params

def setup():
    size(1280, 720)
    
def draw():
    #Canvas
    background(bgcolour)
    mousepressfn()
    translate(width/2+deltax, height/2+deltay)
    
    #Graph
    stroke(pointstroke)
    fill(pointfill)
    ellipse(0, 0, pointr, pointr)
    
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
