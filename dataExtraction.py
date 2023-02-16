def formatData(data):
    data = data.split("\n")
    for i in range(0,len(data)):
        data[i] = data[i].strip()
    return data

inputFile = open("input\\pdh.txt", "r")

fileContents = inputFile.read()

startIndex = fileContents.find("NODES")
endIndex = fileContents.find("\n# LINK SECTION")
nodeData = fileContents[startIndex+8:endIndex-3]

startIndex = fileContents.find("LINKS")
endIndex = fileContents.find("\n# DEMAND SECTION")
linksData = fileContents[startIndex+8:endIndex-3]

startIndex = fileContents.find("DEMANDS")
endIndex = fileContents.find("\n# ADMISSIBLE PATHS SECTION")
demandsData = fileContents[startIndex+10:endIndex-3]

nodeData = formatData(nodeData)
linksData = formatData(linksData)
demandsData = formatData(demandsData)

node_dict = {}
links_dict = {}
demands_dict = {}
for i in nodeData:
    individualData = i.split()
    node_dict[individualData[0]] = {
        "name" : individualData[0],
        "x_coord": float(individualData[2]),
        "y_coord": float(individualData[3])
    }
mod_cap = []
mod_cost = []
for i in linksData:
    mod_cap = []
    mod_cost = []
    individualData = i.split()   
    for index in range(len(individualData)-2,0,-2):
        if individualData[index] != '(':
            mod_cost.append(float(individualData[index]))
            mod_cap.append(float(individualData[index-1]))   
        else:
            break
    mod_cap.reverse()
    mod_cost.reverse()
    links_dict[individualData[0]] = {
        "name" : individualData[0],
        "source" : individualData[2],
        "target" : individualData[3],
        "z_value" : None,
        "link_status" : 1,
        "mod_cost" : mod_cost,
        "mod_cap" : mod_cap
    }

for i in demandsData:
    individualData = i.split()
    demands_dict[individualData[0]] = {
        "name": individualData[0],
        "source": individualData[2],
        "target": individualData[3],
        "demand_value": float(individualData[6])
    }

    graph_dict = {
        "nodes" : dict(node_dict),
        "links" : dict(links_dict),
        "demands" : dict(demands_dict)
    }
print(graph_dict)