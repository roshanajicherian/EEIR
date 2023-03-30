import networkx as nx
def find_new_D_set(graph, demands_dict,e_value):
    d_list = {}
    for key, demand_vector in demands_dict.items():
            demand_value = demand_vector["demand_value"]
            if(demand_value <= e_value):
                 d_list.update(demand_vector)
    return d_list

def reroute(graph, demands_dict):

    status = True
    # For every edge in the graph try bringing the transmission capacity
    # one level down and check if rerouting is possible.
    for u,v,d in graph.edges(data = True):
        source = u
        target  = v
        current_mod_cost = d['z_value']
        current_mod_cost_index = d['mod_cap'].index(current_mod_cost)
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
        for key, demand_vector in new_d_set.items():
             shortest_path_data = demand_vector["shortestPathList"]
             path_list = shortest_path_data['pathList']
             if(path_list[i] == source and path_list[i+1] ==  target):
                      d["resuidal_capacity"]+=demand_vector["demand_value"]
        for key,demand_vector in new_d_set.items():
             source = demand_vector["source"]
             target = demand_vector["target"]
             alt_paths = nx.shortest_simple_paths(graph,source,target) 
    return status