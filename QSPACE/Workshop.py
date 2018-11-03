#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:41:10 2018
@author: eloisechakour
"""
import numpy as np
numpy.random.seed(0)


#Initial Useful variables
expected_average = 6
n = 10

#Define test arrays that will be imported later
def initValMat(n):
    adjmat = np.ones((n, n), dtype=int)
    for i in range(n):
        adjmat[i, i] = 0
    return adjmat
    
def getValArr(adjmat):
    valArr = np.empty((n,))
    for i in range(n):
        valArr[i] = np.sum(adjmat[i], dtype=int)
    return valArr


#Picking an edge to remove
    
    
#Checks if there are any edges left to remove
def checkIfNotDone(adjmat):
    valArr = getValArr(adjmat)
    avgVal = np.sum(valArr)/n
    if avgVal > expected_average:
        return True
    else:
        return False
    
    
#Makes the picking of the vertex somewhat random
def pickRandVertex(eligible_vertices):
     vertex_address = np.random.randint(0, len(eligible_vertices))
     vertex_number = eligible_vertices[vertex_address]
     return vertex_number
                
    
#Tells you which vertex you're removing an edge from
def pickVertex(valArr):
    eligible_vertices = []
        
    for i in range(n):
        if valArr[i] > expected_average:
            eligible_vertices.append(i)
        
    vertex = pickRandVertex(eligible_vertices)
    return vertex


#Pick an edge from the selected vertex
#RETURNS a new matrix with the edge removed
def removeAnEdge(vertex, adjmat):
    valArr = getValArr(adjmat)
    foundLine = False
    i = 0
    while not foundline:
        if valArr[i] > expected_average:
            adjmat[vertex, j] = 0
            adjmat[j, vertex] = 0
            foundline = True
        else:
            i+=1
    return adjmat
    

def executable(n, expected_Average):
    adjMatrix = getValMat(n)
    valArr = getValArr(adjmat)
    while checkIfNotDone == True:
        vertexToRemove = pickVertex(valArr)
        adjMatrix = removeAnEdge(vertexToRemove)
    return adjMatrix