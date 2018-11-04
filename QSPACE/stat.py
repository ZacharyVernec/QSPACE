#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:27:07 2018

@author: eloisechakour
"""

#Have Adj Matrix

#valancy = []
n=10

#Create Valency Array
def valencyArr(n, adjMatrix):
    valencies = []
    val = 0
    for i in range(n):
        for j in range(n):
            val += adjMatrix[i, j]
        valencies.append(val)
    
    
    
    return valencies



#Compute total energy

def energy(valencies, n):
    energy = 0
    for i in range(n):
        energy += (valencies[i])**2
    normEnergy = energy - 36*(n**2)
    return normEnergy
    
#Compute Average Valency
    

def avgVal(valency, adjMatrix):
    edges = 0
    for i in range(n):
        for j in range(n):
            edges += adjMatrix[i, j]
            #implicitly computes factor of 2
    
    alpha = edges/n
    
    return alpha


#Change in distance 















