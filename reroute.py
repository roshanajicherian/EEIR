import networkx as nx
import find_shortest
def find_new_D_set(graph, demands_dict,e_value):
    d_list = {}
    for key, demand_vector in demands_dict.items():
            demand_value = demand_vector["demand_value"]
            if(demand_value <= e_value):
                 d_list.update(demand_vector)
    return d_list

def reroute(graph, demands_dict):

    status = True
    k = 2
    # For every edge in the graph try bringing the transmission capacity
    # one level down and check if rerouting is possible.
    for u,v,d in graph.edges(data = True):
        source = u
        target  = v
        current_mod_cost = d['z_value']
        current_mod_cost_index = d['mod_cap'].index(current_mod_cost)
        graph = find_shortest.findLower(graph)
        graph = find_shortest.findUpper(graph)
        # if the lowest transmission capacity possible is the base transmission
        # then switch of the link and try to route
        if(current_mod_cost_index == 0):
            d["z_value_temp"] = 0 
            d['link_on'] = False
        else:
            d["z_value_temp"] = d['mod_cap'][current_mod_cost_index-1]
        #e_value stores the new total flow value calculated at the new transmission
        #capacity
        d["e_value"] = abs(d['total_flow']-d["z_value_temp"])
        #for each new e_value that is produced find the demands set that
        # satisfy the are within the limits of this value
        new_d_set = find_new_D_set(graph, demands_dict,d["e_value"])
        # For each demand in the new set check if the shortest path for that
        # demand consists of the link (u,v). If yes add dst to the residual capacity
        if(len(new_d_set) > 0):
            shortest_path_data = new_d_set["shortestPathList"]
            path_list = shortest_path_data['pathList']
            for i in range(0, len(path_list)-1):
             if(path_list[i] == source and path_list[i+1] ==  target):
                    d["resuidal_capacity"]+=shortest_path_data["demand_value"]
            source = shortest_path_data["source"]
            target = shortest_path_data["target"]
            alt_paths = nx.all_simple_paths(graph,source,target)
            alt_paths = list(alt_paths)
            alt_paths = sorted(alt_paths, key=lambda path: len(path))
            try:
                kth_shortest_path = alt_paths[k - 1]
            except IndexError:
                return None
    return status, graph