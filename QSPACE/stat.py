#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:27:07 2018

@author: eloisechakour
"""
#import TestFileEloise as t

#Have Adj Matrix

#valancy = []
n=10

#Getting a test adjacency matrix - ignore this it's just to test stuff
#adjMatrix = [[0, 1, 0, 1, 1, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 1, 1, 1, 0, 0],[0, 1, 0, 0, 1, 1, 1, 1, 0, 1],[1, 0, 0, 0, 1, 1, 0, 1, 1, 1],[1, 1, 1, 1, 0, 0, 0, 0, 1, 1],[1, 1, 1, 1, 0, 0, 1, 0, 1, 0],[0, 1, 1, 0, 0 ,1 ,0 ,1, 1, 1],[1, 1, 1, 1, 0, 0, 1, 0, 1, 0],[0, 0, 0, 1, 1, 1, 1, 1, 0, 1],[1, 0, 1, 1, 1, 0, 1, 0, 1, 0]]



#Create Valency Array
def valencyArr(n, adjMatrix):
    valencies = []
    for i in range(n):
        val = 0
        for j in range(n):
            val += adjMatrix[i][j]
        valencies.append(val)
    
    
    
    return valencies



#Compute total energy

def energy(valencies, n):
    energy = 0
    for i in range(n):
        energy += (valencies[i])**2
    normEnergy = energy - 36*n
    return normEnergy
    
#Compute Average Valency
    

def avgVal(valency, adjMatrix):
    edges = 0
    for i in range(n):
        for j in range(n):
            edges += adjMatrix[i][j]
            #implicitly computes factor of 2
    
    alpha = edges/n
    
    return alpha


#Change in distance 
#side1 and side2 are the original path sides as discussed. n is the number of vertices. 

def changeInDist(side1, side2, n):
    dist = (side1**2 + side2**2 + side1*side2)**(0.5)
    diff = side1+side2 - dist
    tot = diff+1
    deltaDist = tot/n
    return deltaDist


"""
from random import randint #problem?
#import math

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
"""

def getOldDist(adjmat, latmat): #DON'T COPY PASTE THIS
	#latmat is the adjmat of a perfect triangular lattice of equal size to adjmat
	n = len(adjmat)	
	for i in range(n):
		for j in range(i, n):
			if adjmat[i][j] == 1 and latmat[i][j] == 0: #new edge!
				#we explore top triangle, so i < j
				#vertex 1 is #i, 2 is #j
				#lattice should be a square lattice (before perturbation
				row_len = int(n**(1/2)) #in vertices
				col1 = i%row_len
				row1 = (i - col1)/row_len
				col2 = j%row_len
				row2 = (j - col2)/row_len
				
				col = abs(col2 - col1)
				row = abs(row2 - row1)
				if not col == 0 and not row == 0:
					row -= 1
	return int(col), int(row)

#d1, d2 = getOldDist(perMatrix, latMatrix)
#print(d1, d2)


#n tot vertices, adjMatrix is unperturbed and pertubed is perturbed 
def executableStats(n, adjMatrix, perturbed):
    valencies = valencyArr(n, adjMatrix)
    E = energy(valencies, n)
    alpha = avgVal(valencies, adjMatrix)
    d1, d2 = getOldDist(perturbed, adjMatrix)
    avgDistChange = changeInDist(d1, d2, n)
    return E, alpha, avgDistChange










