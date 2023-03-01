import networkx as nx
def printGraph(graph):
    with open("graph.txt", "w") as g:
        for u,v,d in graph.edges(data = True):
            g.write(f"u : {u}\tv: {v}\nEdge Data:{d}\n\n\n")
            print(f"u : {u}\tv: {v}\nEdge Data:{d}\n")
