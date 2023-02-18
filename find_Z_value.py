def find_Z_value(graph):
    for u,v,d in graph.edges(data = True):
        if(d["link_on"] == True):
            mod_cap_temp = d["mod_cap"]
            total_flow = d["total_flow"]
            for i in range(0,len(mod_cap_temp)):
                mod_cap_temp[i] = mod_cap_temp[i] - total_flow
            minimum_capacity = min([i for i in mod_cap_temp if i > 0])
            d["z_value"] = minimum_capacity
    return graph