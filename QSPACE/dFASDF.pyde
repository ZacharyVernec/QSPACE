import time
from random import randint
#Canvas params
deltax=0
deltay=0
bgcolour = color(200, 200, 200)
#Graphics params
width = 1280
height = 720
xoffset = 300
yoffset = 300
graphr = 200
pointsep = 100
pointr = 8
pointstrokecol = color(0, 0, 0)
pointfill = color(0, 0, 0)
linestall = 0.1
startstall = 1
unfoldtime = 1
buttonsize = 40
#Model params
sqrtn = 3
n = sqrtn*sqrtn
    
def getord(i, j):
    return j*sqrtn+i
def getcoord(k):
    return k%sqrtn, int(k/sqrtn)

def addedge(mat, i1, j1, i2, j2):
    if i2 >= 0 and j2 >= 0 and i2 < sqrtn and j2 < sqrtn:
        a = getord(i1, j1)
        b = getord(i2, j2)
        mat[a][b] = 1
        mat[b][a] = 1
    
def getlatmat(sqrtn):
    n = sqrtn*sqrtn
    adjmat = [[0 for j in range(n)] for i in range(n)]
    for i in range(sqrtn):
        for j in range(sqrtn):
            addedge(adjmat, i, j, i-1, j)
            addedge(adjmat, i, j, i+1, j)
            addedge(adjmat, i, j, i, j-1)
            addedge(adjmat, i, j, i, j+1)
            if j%2 == 1:
                addedge(adjmat, i, j, i-1, j-1)
                addedge(adjmat, i, j, i-1, j+1)
            else:
                addedge(adjmat, i, j, i+1, j-1)
                addedge(adjmat, i, j, i+1, j+1)
    return adjmat

def getlatcoords(n):
    pixcoords = []
    for k in range(n):
        gridcoord = getcoord(k)
        if gridcoord[1]%2 == 1:
            rowoff = -pointsep/2
        else:
            rowoff = 0
        x = xoffset+rowoff+gridcoord[0]*pointsep
        y = yoffset+gridcoord[1]*pointsep
        pixcoords.append([x, y])
    return pixcoords
                
def getcirccoords(n, r, xoffset, yoffset):
    pixcoords = []
    for i in range(n):
        theta = i*2*PI/n
        x = xoffset+r*cos(theta)
        y = yoffset+r*sin(theta)
        pixcoords.append([x, y])
    return pixcoords

def drawgraph(coordlist, adjmat):
    n = len(adjmat)
    for i in range(n):
        coords1 = coordlist[i]
        ellipse(coords1[0], coords1[1], pointr, pointr)
        for j in range(i, n):
            if adjmat[i][j] == 1:
                coords2 = coordlist[j]
                line(coords1[0], coords1[1], coords2[0], coords2[1])
                
def getAdded(adjmat):
  #returns array of locations where edges need to be added
  added = []
  n = len(adjmat)
  for i in range(n):
    for j in range(i, n):
      if adjmat[i][j] == 0 and i != j:
        added.append([i, j])
  return added

def complete(n):
  #returns a complete graph with n vertices
  complete = [[1 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j:
        complete[i][j] = 0
  return complete

def removeEdge(adjmat, edge):
  #an edge is a 2d array specifying a co-ord on the adjmat
  n = len(adjmat)
  for i in range(n):
    for j in range(n):
      if i == edge[0] and j == edge[1]:
        adjmat[i][j] = 0
        adjmat[j][i] = 0 #don't forget the symmetry!
  return adjmat

def perturb(added, i, j):
  #if we remove an edge, a random edge must be generated (vice versa)
  #this preserves avg valency
  #I add (ie remove from "needs to be removed" list) first
  #(so I don't add back the one I wanted to remove by chance)
  r = randint(0, len(added)-1)
  added.remove(r)
  #i, j specifies an edge to remove,
  #ie an edge that would need to be added to make the graph complete, so
  added.insert(0, [i,j])

  #get an adjmat from this "added" list
  #really added is a list of edges to add to make a comlpete graph
  #so starting at a complete graph and removing accoring to added gets the adjmat  

  #so if we use this perturbed added on a complete graph, using the same loop
  #as for the lattice, we get a perturbed graph
  return added


def setup():
    size(width, height)
    stroke(0)
    fill(0)
    
startTime = time.time() 
laststep = -1
mat_to_plot = complete(n)
def draw():
    background(200, 200, 200)
    global mat_to_plot
    latmat = getlatmat(sqrtn)
    added = getAdded(latmat)
    global startTime
    currtime = time.time()-startTime
    animtime = currtime-(startstall+linestall*len(added))
    startcoords = getcirccoords(n, 200, width/2, height/2)
    endcoords = getlatcoords(n)
    if currtime <= startstall:
        coords = getcirccoords(n, graphr, width/2, height/2)
        drawgraph(coords, mat_to_plot)
    elif currtime <= startstall+linestall*len(added):
        step = int((currtime-startstall)/linestall)
        global laststep
        if step > laststep and step<len(added):
            mat_to_plot = removeEdge(mat_to_plot, added[step])
        coords = getcirccoords(n, graphr, width/2, height/2)
        drawgraph(coords, mat_to_plot)
        laststep = step
    elif currtime <= startstall+linestall*len(added)+unfoldtime:
        def subfn(l1, l2):
            temp = lambda li1, li2: li1-li2
            return map(temp, l1, l2)
        coordvecs = map(subfn, endcoords, startcoords)
        dcoordvecs = [[coordvecs[k][0]*float(float(animtime)/unfoldtime), coordvecs[k][1]*float(float(animtime)/unfoldtime)] for k in range(n)]
        print(dcoordvecs)
        def addfn(l1, l2):
            temp = lambda li1, li2: li1+li2
            return map(temp, l1, l2)
        currcoords = map(addfn, startcoords, dcoordvecs)
        print(currcoords)
        drawgraph(currcoords, mat_to_plot)
    else:
        drawgraph(endcoords, mat_to_plot)
    
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
