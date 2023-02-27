import sndlib_model, find_shortest_path, os, find_Z_value
import networkx as nx
import matplotlib.pyplot as plt
# Creting graph and demands_dict
demands_dict, graph = sndlib_model.create_graph(f"{os.getcwd()}/input/pdh.txt")
# print(demands_dict,graph)
# Finding the shortest path and calculating total flow 
demands_dict, graph =  find_shortest_path.find_shortest(demands_dict,graph)
# Finding zValue for each edge within the graph
nx.draw_spring(graph,with_labels = True)
plt.show()
graph = find_Z_value.find_Z_value(graph)
print(graph.edges(data = True))