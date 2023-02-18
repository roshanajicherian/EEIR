import sndlib_model, find_shortest_path, os, find_Z_value
demands_dict, graph = sndlib_model.create_graph(f"{os.getcwd()}\\input\\pdh.txt")
# print("Demands Dictionary : ", demands_dict)
# print(demands_dict,graph)
demands_dict, graph =  find_shortest_path.find_shortest(demands_dict,graph)
graph = find_Z_value.find_Z_value(graph)
print(graph.edges(data = True))