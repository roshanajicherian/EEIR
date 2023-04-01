import sndlib_model, os, find_shortest,printer, reroute
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image

def runner(topology):
    # Creting graph and demands_dict
    demands_dict, graph = sndlib_model.create_graph(f"{os.getcwd()}/input/{topology}.txt")
    # print(demands_dict,graph)
    # Finding the shortest path and calculating total flow 
    demands_dict, graph =  find_shortest.find_shortest(demands_dict,graph)
    #prinitng and plotting graph data
    printer.printGraph(graph)
    printer.plotGraph(graph)
    reroute.reroute(graph,demands_dict)


def confirmButton():
    global initialImage
    global initialImageLabel
    runner(topology=str(clicked.get()))
    initialImage = ImageTk.PhotoImage(Image.open("images/initialConfig.png"))
    initialImageLabel = Label(image=initialImage)
    initialImageLabel.grid(row=3,column=0)


root = Tk()
root.geometry("1440x900")
root.title("AI Assisted Energy Efficent Wirless Routing Algorithm")

# Creating Dropdown menu to select the network topolgy
options = ["pdh" , "COST266", "di-yuan"]

clicked = StringVar()
clicked.set("pdh")

topologyDropDown = OptionMenu(root, clicked, *options)
topolgySelectLabel = Label(root,text="Select Topolgy")
topolgySelectLabel.grid(row=0,column=0, padx=10, pady=10)
topologyDropDown.grid(row=0,column=1,padx=10,pady=10)

#Confirm button to run the algorithm on the code
confirmButton = Button(root,text="Confirm", padx=20, pady=20, command=confirmButton)
confirmButton.grid(row=1,column=0, columnspan=2)
#3 images. One before running the algorithm. The intial weights, final weights and 
# other metric

#Exit button
exitButton = Button(root,text= "EXIT", command=root.quit)
exitButton.grid(row=1,column=2)

root.mainloop()
    