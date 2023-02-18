import sndlib_model
import find_shortest_path
import os
demands_dict, graph = sndlib_model.create_graph(f"{os.getcwd()}\\input\\pdh.txt")
# print("Demands Dictionary : ", demands_dict)
# print(demands_dict,graph)
find_shortest_path.find_shortest(demands_dict,graph)