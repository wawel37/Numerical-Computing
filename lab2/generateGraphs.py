import networkx as nx
import random

def configureGraph(G):
    a, b = random.choice(list(G.edges))
    SEMEdge = G.edges[a, b]
    SEMEdge['index'] = 'E'
    SEMEdge['nodeFrom'] = SEMEdge['nodeTo'] = -1
    SEMEdge['voltage'] = random.randint(1,100)

    index = 0
    for (start, stop) in G.edges:
        edge = G.edges[start, stop]
        if 'voltage' in edge:
            continue
        R = random.randint(1, 10)
        edge['resistance'] = R
        edge['index'] = index
        edge['nodeFrom'] = edge['nodeTo'] = -1
        index += 1

    return G
    
def generateErdos(n, p):
    G = nx.erdos_renyi_graph(n, p)

    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(n, p)
    
    configureGraph(G)
    return G

def generateCubic(n):
    G = nx.random_regular_graph(3,n)
    configureGraph(G)
    return G

def generateGrid(m, n):
    G = nx.grid_2d_graph(m,n)
    configureGraph(G)
    return G

def generateSmallWorld(n):
    G = nx.connected_watts_strogatz_graph(n, n//2, 1)
    configureGraph(G)
    return G

def generateBridge(n, p):
    G1 = nx.erdos_renyi_graph(n, p)
    while not nx.is_connected(G1):
        G1 = nx.erdos_renyi_graph(n, p)

    G2 = nx.erdos_renyi_graph(n, p)
    while not nx.is_connected(G2):
        G2 = nx.erdos_renyi_graph(n, p)
    
    node1 = random.choice(list(G1.nodes))
    node2 = random.choice(list(G2.nodes))

    G1.add_edge(node1, node2)

    G3 = nx.compose(G1, G2)

    configureGraph(G3)
    return G3


