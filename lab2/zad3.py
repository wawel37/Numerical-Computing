import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from generateGraphs import *

# IMPORTANT

# TESTED WITH decorator 4.4.2

def loadGraphFromFile(fileName, s, t, V):
    G = nx.Graph()

    with open(fileName, "r") as file:
        edges = file.readlines()

        index = 0
        for edge in edges:
            content = edge.split()
            G.add_node(content[0])
            G.add_node(content[1])
            if (content[0] == s and content[1] == t) or (content[0] == t and content[1] == s):
                G.add_edge(content[0], content[1], index='E', nodeFrom = -1, nodeTo = -1, voltage = V)
            else:
                G.add_edge(content[0], content[1], index = index, resistance = content[2], nodeFrom = -1, nodeTo = -1)
                index += 1
    print(len(G.edges))
    return G

def checkIfPartOfSEMEdge(G, node):
    for (start, stop) in G.edges(node):
        edge = G.edges[start, stop]
        if 'voltage' in edge:
            return True
    return False

def prepareMatrices(G):
    N = len(G.edges) - 1
    A = np.zeros((N,N))
    B = np.zeros((N))

    row = 0
    simpleCycles = nx.cycle_basis(G)
    for cycle in simpleCycles:
        cycle.append(cycle[0])
        for node in range(len(cycle) - 1):
            start = cycle[node]
            stop = cycle[node + 1]
            edge = G.edges[start,stop]            
            if 'voltage' not in edge:
                if edge['nodeFrom'] == -1:
                    edge['nodeFrom'] = start
                    edge['nodeTo'] = stop

                A[row][edge['index']] = edge['resistance']
                if not (edge['nodeFrom'] == start and edge['nodeTo'] == stop):
                    A[row][edge['index']] *= (-1)
            else:
                B[row] = edge['voltage']
        row += 1

    for node in G.nodes:
        if checkIfPartOfSEMEdge(G, node):
            continue
        for (start, stop) in G.edges(node):
            edge = G.edges[start, stop]
            start = edge['nodeFrom']
            stop = edge['nodeTo']
            value = 1
            if node != edge['nodeTo']:
                value *= (-1)
            
            A[row][edge['index']] = value
        row += 1
    return A, B
    
def drawGraph(diG):
    if nx.check_planarity(diG)[0]:
        pos = nx.planar_layout(diG)
    else:
        pos = nx.spring_layout(diG)

    nx.draw_networkx_nodes(diG, pos)
    nx.draw_networkx_labels(diG, pos)
    nx.draw_networkx_edges(diG, pos)
    lables = nx.get_edge_attributes(diG, 'current')
    nx.draw_networkx_edge_labels(diG, pos, edge_labels = lables)
    plt.show()

def getDirectedGraph(G, I):
    diG = nx.DiGraph()

    index = 0
    for (start, stop) in G.edges:
        edge = G.edges[start, stop]
        if 'voltage' not in edge:
            if I[index] < 0:
                edge['nodeFrom'], edge['nodeTo'] = edge['nodeTo'], edge['nodeFrom']
                I[index] *= -1
            diG.add_edge(edge['nodeFrom'], edge['nodeTo'], current = round(I[edge['index']], 3))
            index += 1
        else:
            diG.add_edge(start, stop, current = None)
            diG.add_edge(stop, start, current = None)
    
    return diG

s, t, V = '1', '2', '10'
#G = loadGraphFromFile("graph.txt", s, t, V)
#G = generateErdos(20,0.5)
#G = generateCubic(3, 3*2*5)

while 1:
    G = generateBridge(10, 0.5)
    A, B = prepareMatrices(G)
    solved = np.linalg.solve(A, B)
    diG = getDirectedGraph(G, solved)
    print(A)
    print(B)
    print(solved)
    drawGraph(diG)


