import networkx as nx
import matplotlib.pyplot as plt

def printGraph(graph):
    with open("graph.txt", "w") as g:
        for u,v,d in graph.edges(data = True):
            g.write(f"u : {u}\tv: {v}\nEdge Data:{d}\n\n\n")
            # print(f"u : {u}\tv: {v}\nEdge Data:{d}\n")

def plotGraph(graph):
    pos = nx.shell_layout(graph)
    nx.draw(graph,pos,with_labels = True, 
            node_color = "red", font_color = "white", node_size = 800, 
            width = 2.0, edge_color = "grey")
    edge_weights = {(u,v) : d["total_flow"] for u,v,d in graph.edges(data= True)}
    nx.draw_networkx_edge_labels(graph,pos,edge_weights, label_pos= 0.5)
    # plt.figure(figsize=(10,10))
    plt.figtext(0.5, 0.01, "Total Flow", wrap=True, horizontalalignment='center', fontsize=12)

    plt.savefig("images/totalFlow.png")
    plt.figure().clear()

    nx.draw(graph,pos,with_labels = True, 
            node_color = "blue", font_color = "white", node_size = 800, 
            width = 2.0, edge_color = "grey")
    edge_weights = {(u,v) : d["z_value"] for u,v,d in graph.edges(data= True)}    
    nx.draw_networkx_edge_labels(graph,pos,edge_weights, label_pos= 0.5)
    plt.figtext(0.5, 0.01, "Transmission Capacity (Initial)", wrap=True, horizontalalignment='center', fontsize=12)
    plt.savefig("images/transmissionCapacityInitial.png")
    plt.figure().clear()
    nx.draw(graph,pos,with_labels = True, 
            node_color = "green", font_color = "white", node_size = 800, 
            width = 2.0, edge_color = "grey")
    
    edge_weights = {(u,v) : d["updated_tranmission"] for u,v,d in graph.edges(data= True)}
    nx.draw_networkx_edge_labels(graph,pos,edge_weights, label_pos= 0.5)
    plt.figtext(0.5, 0.01, "Transmission Capacity (Final)", wrap=True, horizontalalignment='center', fontsize=12)
    plt.savefig("images/transmissionCapacityFinal.png")
    plt.figure().clear()

    

