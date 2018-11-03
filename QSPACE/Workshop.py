#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:41:10 2018
@author: eloisechakour
"""
import numpy as np
#numpy.random.seed(0)


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
        valArr[i] = n-1
    #for i in range(n):
        #valArr[i] = np.sum(adjmat[i], dtype=int)
    return valArr


#Picking an edge to remove
    
    
#Checks if there are any edges left to remove
def checkIfNotDone(adjmat, valArr):
    cont = 0
    for i in range(len(valArr)):
        if valArr[i] > expected_average:
            cont = 1
    
    return cont
    
    
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
def removeAnEdge(vertex, adjmat, valArr):
    stop = 0
    i = 0
    
    while stop == 0:
        #print(vertex)
        if adjmat[vertex, i] == 1:
            
            if valArr[i] > expected_average:
                adjmat[vertex, i] = 0
                adjmat[i, vertex] = 0
                valArr[vertex] -=1
                valArr[i] -=1
                stop = 1
                print("In the removeAnEdge Loop Case 1")
                break
            else:
                print("In the removeAnEdge Loop Case 1")
                i+=1
    return adjmat
    

def executable(n, expected_Average):
    adjMatrix = initValMat(n)
    valArr = getValArr(adjMatrix)
    adjMatricesOverTime = [adjMatrix]
    done = 1
    while done == 1:
        done=0
        vertexToRemove = pickVertex(valArr)
        adjMatrix2 = removeAnEdge(vertexToRemove, adjMatrix, valArr)
        done = checkIfNotDone(adjMatrix2, valArr)
        adjMatricesOverTime.append(adjMatrix2)
        print("Continue Variable = " + str(done))
    return adjMatricesOverTime, print("Done!")


finalMatrix = executable(n, expected_average)