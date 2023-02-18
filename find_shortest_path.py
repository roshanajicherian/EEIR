import networkx as nx
import matplotlib.pyplot as plt

def find_shortest(demands_dict, graph):
    demands = demands_dict
    for key, demand_vector in demands_dict.items():
        source = demand_vector["source"]
        target = demand_vector["target"]
        print(nx.dijkstra_path(graph,source, target))
    nx.draw_spring(graph,with_labels = True)
    plt.show()