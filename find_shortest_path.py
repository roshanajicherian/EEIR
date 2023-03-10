import networkx as nx
import matplotlib.pyplot as plt
shortestPathList = []

def find_demand(start,end,demands_dict):
    # Simple function to find the demand value given a source and destination
    for key, demand_vector in demands_dict.items():
        if demand_vector["source"] == start and demand_vector["target"] == end:
            return demand_vector["demand_value"]
        
def compute_total_flow(u,v, shortestPathList, demands_dict):
    # Function to compute the total flow through each link in the graph
    total_flow = 0
    for i in shortestPathList:
        temp = i['pathList']
        # TODO: POSSIBLE ERROR OVER HERE
        for j in range(0,len(temp)-1):
            if u== temp[j] and v==temp[j+1]:
                total_flow+=find_demand(u,v, demands_dict)
    return total_flow
        
def find_shortest(demands_dict, graph):
    for key, demand_vector in demands_dict.items():
        source = demand_vector["source"]
        target = demand_vector["target"]
        # Calculate the shortest path from the source to destination using dijkstra's algorithm
        # The path list is obtained using the function
        path_list = nx.dijkstra_path(graph,source, target)
        shortestPathList.append({"source" : source,
                                 "target" : target,
                                 "pathList" : path_list})
        # Add the path_list to demands_dict
        demand_vector["pathList"] = path_list
    for u,v,d in graph.edges(data = True):
        # if u,v is a part of the shortestpathist of any demand then add that the total flow of u,v
        d["total_flow"] = compute_total_flow(u,v, shortestPathList, demands_dict)
    # nx.draw_circular(graph,with_labels = True)
    # plt.show()
    for u,v,d in graph.edges(data = True):
        # if there is no flow in the links, turn of the links
        if(d["total_flow"] == 0):
            d["link_on"] = False
    return [demands_dict, graph]