def findLowerTransmission(demands_dict,graph):
    count = 0
    for u,v,d in graph.edges(data = True):
        current = d["z_value"]
        modCaps = d["mod_cap"]
        modIndex = modCaps.find(current)
        if count%5==0:
            if(modIndex-1>0):
                d["updated_tranmission"] = modCaps[modIndex-1]
            else:
                d["updated_tranmission"] = modCaps[modIndex]
        count+=1

