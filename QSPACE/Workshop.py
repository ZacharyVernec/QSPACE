#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:41:10 2018

@author: eloisechakour
"""

import numpy as np
import random as rand


#Initial Useful variables
expected_average = 6
n = 10

#Define test arrays that will be imported later
def valFct(n):
    valency = np.zeros[n]

    for i in range[len(valency)]:
        valency[i] = n-1
    
    return valency
    
smallPointArray = []
bigPointArray = []
sliceOfMatrix = []
adjMatrix = []




#Picking an edge to remove
    
    
#Checks if there are any edges left to remove
def checkContinue():
    remove = 1
    for i in range[len(valency)]:
        if valency[i] > expected_average:
            remove ==1
        else: 
            remove = 0
    
    return remove
    
    
#Makes the picking of the vertex somewhat random
def pickRandVertex(eligible_vertices):
     vertex_address = rand.randint(0, len(eligible_vertices))
     vertex_number = eligible_vertices[vertex_address]
     return vertex_number
                
    
#Tells you which vertex you're removing an edge from
def pickVertex(valency):
    eligible_vertices = []
        
    for j in range[len(valency)]:
        if valency[j] > expected_average:
            eligible_vertices.append[j]
        
    vertex = pickRandVertex(eligible_vertices)
    return vertex


#Pick an edge from the selected vertex
def pickEdge(vertex, sliceOfMatrix, valency):
    foundLine = 0
    while foundLine ==0:
        i = 0
        if sliceOfMatrix[i] == 1:
            if valency[i] > expected_average:
                valency[vertex] -=1
                valency[i] -= 1
                sliceOfMatrix[i] = 0
                break
        else:
            i+=1
    

def executable(adjMatrix, expected_Average, n):
    valency = valFct(n)
    remove = checkContinue()
    while remove ==1:
        vertex = pickVertex(valency)
        #this is probably wrong
        sliceOfMatrix = adjMatrix[vertex]
        pickEdge(vertex, sliceOfMatrix, valency)
        adjMatrix[vertex] = sliceOfMatrix
    
    return adjMatrix
        




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





