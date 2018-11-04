def getAdded(adjmat):
	#returns array of locations where edges need to be added
	added = []
	n = len(adjmat)
	for i in range(n):
		for j in range(n):
			if adjmat[i][j] == 0:
				added.append([i, j])
	return added

def complete(n):
	#returns a complete graph with n vertices
	one_row = [1 for i in range(n)]
	complete = [one_row for i in range(n)]
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

#a main loop should...
#
#1- run added = getAdded(adjmat) on a given adjmat
#
#2- get a mat_to_plot = complete() adjmat
#
#3- for every value in added, run removeEdge(mat_to_plot, added[i])
#
#4- 	plot mat_to_plot as a graph with vertices arranged in a circle
#
#5- when for done, plot mat_to_plot as a triangular lattice
