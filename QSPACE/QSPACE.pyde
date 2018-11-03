#Canvas params
deltax=0
deltay=0
bgcolour = color(200, 200, 200)
#Graphics params
pointxoffset = 400
pointyoffset = 140
pointsep = 50
pointr = 10
pointstrokecol = color(0, 0, 0)
pointfill = color(255, 255, 255)
#Model params
nverts = 100

def setup():
    size(1280, 720)
    
def buildmat(n):
    vertmatrix = []
    for i in range(n):
        vertmatrix.append([])
        for j in range(n):
            vertmatrix[i].append(0)
    return vertmatrix
mat = buildmat(nverts)
def drawverts(n, xoffset, yoffset, sep, r):
    for i in range(int(sqrt(n))):
        for j in range(int(sqrt(n))):
            if i%2 == 0:
                ellipse(xoffset+sep/2+j*sep, yoffset+i*sep, r, r)
            else: 
                ellipse(xoffset+j*sep, yoffset+i*sep, r, r)
    
def draw():
    #Canvas
    background(bgcolour)
    mousepressfn()
    translate(deltax, deltay)
    
    #Graph
    stroke(pointstrokecol)
    fill(pointfill)
    drawverts(nverts, pointxoffset, pointyoffset, pointsep, pointr)
    
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
