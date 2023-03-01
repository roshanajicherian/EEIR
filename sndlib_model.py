import networkx as nx
import matplotlib.pyplot as plt
import find_shortest_path
graph = nx.Graph()

def format_data(data):
    data = data.split("\n")
    for i in range(0,len(data)):
        data[i] = data[i].strip()
    return data


def create_graph(filename):
# Opening and reading the cotnets of the file in READ mode
    input_file = open(filename, "r")

    file_contents = input_file.read()
# Finding the nodes section and adding everything within the nodes section into nodes_data 
    start_index = file_contents.find("NODES")
    end_index = file_contents.find("\n# LINK SECTION")
    node_data = file_contents[start_index+8:end_index-3]

# Finding the links section and adding everything within the links section into link_data 
    start_index = file_contents.find("LINKS")
    end_index = file_contents.find("\n# DEMAND SECTION")
    link_data = file_contents[start_index+8:end_index-3]

# Finding the demands section and adding everything within the demands section into demands_data 
    start_index = file_contents.find("DEMANDS")
    end_index = file_contents.find("\n# ADMISSIBLE PATHS SECTION")
    demands_data = file_contents[start_index+10:end_index-3]

#Formating the data using the format_data function
    node_data = format_data(node_data)
    link_data = format_data(link_data)
    demands_data = format_data(demands_data)

# Creating dictionaries to store the data as key value pairs. Split the data 
# based on whitespaces and then add the data into corresponding varibles
    demands_dict = {}
    for i in node_data:
        individual_data = i.split()
        graph.add_nodes_from([(individual_data[0], 
                        {"x_coord" : float(individual_data[2]),
                         "y_coord" : float(individual_data[3])})])
# Multiple mod_cap and mod_cost exist for a single link. Creating arrays to store these
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
        graph.add_edge(individual_data[2],
                       individual_data[3], 
                       z_value = None,
                       link_on = True,
                       mod_cost = mod_cost,
                       mod_cap = mod_cap,
                       dst = 0,
                       weight = 1)
    for i in demands_data:
        individual_data = i.split()
        demands_dict[individual_data[0]] = {
            "name": individual_data[0],
            "source": individual_data[2],
            "target": individual_data[3],
            "demand_value": float(individual_data[6])
        }
    # print(graph.edges.keys())
    # print(graph.nodes(data= True))
    # print(graph)
    # nx.draw_spring(graph,with_labels = True)
    # plt.show()
    return [demands_dict, graph]