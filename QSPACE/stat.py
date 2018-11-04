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




def executableStats(n, adjMatrix):
    valencies = valencyArr(n, adjMatrix)
    E = energy(valencies, n)
    alpha = avgVal(valencies, adjMatrix)
    avgDistChange = changeInDist(2, 4, n)
    return E, alpha, avgDistChange










