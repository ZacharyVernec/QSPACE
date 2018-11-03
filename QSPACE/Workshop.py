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

#Define a test array that will be imported later
valency = np.zeros[n]

for i in range[len(valency)]:
    valency[i] = n-1




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
    
    
#Makes the picking of the edge somewhat random
def pickRandEdge(eligible_vertices):
     edge_address = rand.randint(0, len(eligible_vertices))
     edge_number = eligible_vertices[edge_address]
     return edge_number
                
    
#Tells you which edge you're removing    
def pickEdge(remove):
    eligible_vertices = []
        
    for j in range[len(valency)]:
        if valency[j] > expected_average:
            eligible_vertices.append[j]
        
    edge = pickRandEdge(eligible_vertices)
    return edge









        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





