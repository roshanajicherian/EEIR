import networkx as nx
import copy 
shortestPathList = []

def find_z_value(graph):
    for u,v,d in graph.edges(data = True):
        if(d["link_on"] == True):
            mod_cap_temp = copy.copy(d["mod_cap"])
            total_flow = abs(d["total_flow"])
            for i in range(0,len(mod_cap_temp)):
                mod_cap_temp[i] = mod_cap_temp[i] - total_flow
            # Finding minimum possible positive value i.e. finding the closest value to total_flow
            minimum_capacity = min([i for i in mod_cap_temp if i > 0])
            d["z_value"] = minimum_capacity + total_flow
            d["resuidal_capacity"] = minimum_capacity 
    return graph

def findTotalCost(pathList, graph):
    totalCost = 0
    for i in range(0, len(pathList)-1):
        start = pathList[i]
        end = pathList[i+1]
        for u,v,d in graph.edges(data = True):
            if (u==start and v ==end) or (u==end and v==start):
                totalCost+=(d["mod_cap"][0])
    return totalCost

def find_dst(graph, shortestPathList):
    with open("weight.txt", "w") as wei:
        #For every shortest path that has been generated do the follwing
        for i in range(0,len(shortestPathList)):
            source = shortestPathList[i]['source']
            target = shortestPathList[i]['target']
            for u in shortestPathList[i]['pathList']:
                # For each node in the shortest path list find all the neigbhours of that node
                neighboursList = [n for n in graph.neighbors(u)]
                for k in neighboursList:
                    # Set the value of dst and total flow based on the eqauation given
                    if u==source:
                        temp = -shortestPathList[i]['demandValue']
                        graph[u][k]['total_flow']+=(-shortestPathList[i]['demandValue'])
                    elif u==target:
                        temp = shortestPathList[i]['demandValue']
                        graph[u][k]['total_flow']+=(shortestPathList[i]['demandValue'])
                    else:
                        temp = 0
                        graph[u][k]['total_flow']+=0
                    #!!Debugging Code
                    if((u== "N9" and k == "N2") or (u=="N2" and k == "N9")):
                        wei.write(f"Source : {source}\t\tTarget: {target}\nPath List : {shortestPathList[i]['pathList']}\nu : {u}\nk: {k}\nValue : {temp}\nFinal: {graph[u][k]['total_flow']}\n\n")
    for u,v,d in graph.edges(data = True):
        if(d["total_flow"] == 0):
            d["link_on"] = False
    return graph



def find_fst(start,end,graph):
    for u,v,d in graph.edges(data = True):
            if (u==start and v ==end):
                return 1
            elif (u==end and v==start):
                return -1

def find_shortest(demands_dict, graph):
    with open("output.txt", "w") as f:
        with open("errors.txt", "w") as e:
            for key, demand_vector in demands_dict.items():
                source = demand_vector["source"]
                target = demand_vector["target"]
                # Calculate the shortest path from the source to destination using dijkstra's algorithm
                # The path list is obtained using the function
                path_list = nx.dijkstra_path(graph,source, target)
                path_length = nx.dijkstra_path_length(graph,source, target)
                totalCost = findTotalCost(path_list, graph)
                demandValue = demand_vector["demand_value"]
                #!Debugging Code
                f.write(f"Source: {source}\tTarget: {target}\nPath List: {path_list}\nPath Length : {path_length}\nTotal Cost: {totalCost}\nDemand Value: {demandValue}\n")
                #TODO: Possible change over here in COST266
                if(totalCost<=demand_vector["demand_value"]):
                    data = {"source" : source,
                            "target" : target,
                            "pathList" : path_list,
                            "pathLength" : path_length,
                            "totalCost" : totalCost,
                            "demandValue" : demandValue,
                            "dst" : 0}
                    shortestPathList.append(data)
                    # Add the path_list to demands_dict
                    demand_vector["shortestPathList"] = data
                else:
                    #!Debugging Code
                    e.write(f"Source: {source}\tTarget: {target}\nPath List: {path_list}\nPath Length : {path_length}\nTotal Cost: {totalCost}\nDemand Value: {demandValue}\n")
            graph = find_dst(graph,shortestPathList)
            graph = find_z_value(graph)
    return [demands_dict, graph]