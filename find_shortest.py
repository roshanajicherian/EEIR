import networkx as nx
shortestPathList = []

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
    for i in range(0,len(shortestPathList)):
        source = shortestPathList[i]['source']
        target = shortestPathList[i]['target']
        for j in shortestPathList[i]['pathList']:
            neighboursList = [n for n in graph.neighbors(j)]
            for k in neighboursList:
                if j==source:
                    graph[j][k]['dst']+=(-shortestPathList[i]['demandValue'])
                elif j==target:
                    graph[j][k]['dst']+=(shortestPathList[i]['demandValue'])
                else:
                    graph[j][k]['dst']+=0
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
                f.write(f"Source: {source}\tTarget: {target}\nPath List: {path_list}\nPath Length : {path_length}\nTotal Cost: {totalCost}\nDemand Value: {demandValue}\n")
                if(totalCost<=demand_vector["demand_value"]):
                    shortestPathList.append({"source" : source,
                                            "target" : target,
                                            "pathList" : path_list,
                                            "pathLength" : path_length,
                                            "totalCost" : totalCost,
                                            "demandValue" : demandValue,
                                            "dst" : 0})
                    # Add the path_list to demands_dict
                    # TODO: Add everything else also(not just pathList)
                    demand_vector["shortestPathList"] = shortestPathList
                else:
                    e.write(f"Source: {source}\tTarget: {target}\nPath List: {path_list}\nPath Length : {path_length}\nTotal Cost: {totalCost}\nDemand Value: {demandValue}\n")
            graph = find_dst(graph,shortestPathList)
    return [demands_dict, graph]