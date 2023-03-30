import sndlib_model, os, find_shortest,printer, reroute
import networkx as nx
import matplotlib.pyplot as plt
# Creting graph and demands_dict
demands_dict, graph = sndlib_model.create_graph(f"{os.getcwd()}/input/pdh.txt")
# print(demands_dict,graph)
# Finding the shortest path and calculating total flow 
demands_dict, graph =  find_shortest.find_shortest(demands_dict,graph)
printer.printGraph(graph)
# printer.plotGraph(graph)
reroute.reroute(graph,demands_dict)