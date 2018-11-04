#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:41:10 2018
@author: eloisechakour
"""
import numpy as np
np.random.seed(0)


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

'''
#Pick an edge from the selected vertex
#RETURNS a new matrix with the edge removed
def removeAnEdge(vertex, adjmat, valArr):
    stop = 0
    i = 0
    
    while adjmat[vertex, i] == 1 and stop == 0:
        #print(vertex)   
        print("still in loop here...")        
        if valArr[i] > expected_average:
            adjmat[vertex, i] = 0
            adjmat[i, vertex] = 0
            valArr[vertex] -=1
            valArr[i] -=1
            stop = 1
        else:
            print("in else case")
            i+=1
    return adjmat

''' 
def removeAnEdge(vertex, adjmat, valArr):
    row = adjmat[vertex]
    for i in range(0, len(row)-1):
        if row[i] == 1 and valArr[i] > expected_average:
            adjmat[vertex, i] = 0
            adjmat[i, vertex] = 0
            valArr[vertex] -=1
            valArr[i] -=1
            return adjmat
        

def executable(n, expected_Average):
    adjMatrix = initValMat(n)
    valArr = getValArr(adjMatrix)
    adjMatricesOverTime = [adjMatrix]
    running = 1
    while running:
        vertexToRemove = pickVertex(valArr)
        adjMatrix2 = removeAnEdge(vertexToRemove, adjMatrix, valArr)
        adjMatricesOverTime.append(adjMatrix2)
        running = checkIfNotDone(adjMatrix2, valArr)
        #print("Continue Variable = " + str(running))
        print(valArr)
    return adjMatricesOverTime, print("Done!")


matrices = executable(n, expected_average)

def toGEXF(adjMatricesOverTime):
    with open('startGEXF.txt', 'r') as template:
        startstr = template.read()
    nowstr = str(int(time.time()))
    
    endoftheworld = len(adjMatricesOverTime)
    with open(nowstr, 'w') as file:
        file.write(startstr)
        file.write('    <nodes>')
        for i in range(n):
            file.write('      <node id="'+str(i)+'" label="Node '+str(i)+'" start="0" endopen="'+str(endoftheworld)+'" />')
        file.write('    </nodes>')
        file.write('    <edges>')
        edgeEndTimes = sum(adjMatricesOverTime)
        for i in range(n):
            for j in range(n):
                if j >= i: #check if in upper triangle
                    file.write('<edge source="'+str(i)+'" target="'+str(j)+'" start="0" endopen="'+str(edgeEndTimes[i, j])+'"/>')
        file.write('    </edges>')
        file.write('  </graph>')
        file.write('</gexf>')
toGEXF(matrices)