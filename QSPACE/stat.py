#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:27:07 2018

@author: eloisechakour
"""

#Have valancy

valancy = []
n=10


#Compute total energy

def energy(valency, n):
    energy = 0
    for i in range(n):
        energy += (valency[i])**2
    
    return energy
    

#Compute Average Valency
    

def avgVal(valency, adjArr):
    edges = 0
    for i in range(n):
        for j in range(n):
            edges += adjArr[i, j]
            #implicitly computes factor of 2
    
    alpha = edges/n
    
    return alpha


