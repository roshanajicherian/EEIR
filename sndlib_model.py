def formatData(data):
    data = data.split("\n")
    for i in range(0,len(data)):
        data[i] = data[i].strip()
    return data


def create_graph(filename):
    input_file = open(filename, "r")

    file_contents = input_file.read()

    start_index = file_contents.find("NODES")
    end_index = file_contents.find("\n# LINK SECTION")
    node_data = file_contents[start_index+8:end_index-3]

    start_index = file_contents.find("LINKS")
    end_index = file_contents.find("\n# DEMAND SECTION")
    link_data = file_contents[start_index+8:end_index-3]

    start_index = file_contents.find("DEMANDS")
    end_index = file_contents.find("\n# ADMISSIBLE PATHS SECTION")
    demands_data = file_contents[start_index+10:end_index-3]

    node_data = formatData(node_data)
    link_data = formatData(link_data)
    demands_data = formatData(demands_data)

    node_dict = {}
    links_dict = {}
    demands_dict = {}
    for i in node_data:
        individual_data = i.split()
        node_dict[individual_data[0]] = {
            "name" : individual_data[0],
            "x_coord": float(individual_data[2]),
            "y_coord": float(individual_data[3])
        }
    mod_cap = []
    mod_cost = []
    for i in link_data:
        mod_cap = []
        mod_cost = []
        individual_data = i.split()
        for index in range(len(individual_data)-2,0,-2):
            if individual_data[index] != '(':
                mod_cost.append(float(individual_data[index]))
                mod_cap.append(float(individual_data[index-1]))
            else:
                break
        mod_cap.reverse()
        mod_cost.reverse()
        links_dict[individual_data[0]] = {
            "name" : individual_data[0],
            "source" : individual_data[2],
            "target" : individual_data[3],
            "z_value" : None,
            "link_status" : 1,
            "mod_cost" : mod_cost,
            "mod_cap" : mod_cap
        }

    for i in demands_data:
        individual_data = i.split()
        demands_dict[individual_data[0]] = {
            "name": individual_data[0],
            "source": individual_data[2],
            "target": individual_data[3],
            "demand_value": float(individual_data[6])
        }

        graph_dict = {
            "nodes" : dict(node_dict),
            "links" : dict(links_dict),
            "demands" : dict(demands_dict)
        }

    return(graph_dict)

