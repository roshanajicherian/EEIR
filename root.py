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
    status, graph = reroute.reroute(graph,demands_dict)
    printer.plotGraph(graph)
    printer.printGraph(graph)

def back():
    global my_label, myImage1, myImage2, myImage3,button_back,button_exit,button_forward
    global next_image, prev_image, totalImages, image_list
    my_label.grid_forget()
    next_image-=1
    prev_image-=1
    my_label = Label(outputFrame1,image=image_list[prev_image])
    button_forward = Button(outputFrame1,text = ">>", command=forward)
    if(prev_image>=1):
        button_back = Button(outputFrame1,text="<<", command= back)
    else:
        button_back = Button(outputFrame1,text="<<", state=DISABLED)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=1)
    my_label.grid(row=0,column=0,columnspan=2)
    

def forward():
    global my_label, myImage1, myImage2, myImage3,button_back,button_exit,button_forward
    global next_image, prev_image, totalImages, image_list
    my_label.grid_forget()   
    next_image+=1
    prev_image+=1
    my_label = Label(outputFrame1,image=image_list[next_image])
    button_back = Button(outputFrame1,text = "<<", command=back)
    if(next_image<totalImages-1):
        button_forward = Button(outputFrame1,text=">>", command= forward)
    else:
        button_forward = Button(outputFrame1,text=">>", state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=2)
    # my_label.pack()
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=1)
    

def confirmButton():
    global my_label, myImage1, myImage2, myImage3,button_back,button_exit,button_forward
    global image_list, totalImages, current_image, next_image, prev_image
    runner(topology=str(clicked.get()))
    myImage1= ImageTk.PhotoImage(Image.open("images/totalFlow.png"))
    myImage2= ImageTk.PhotoImage(Image.open("images/transmissionCapacityInitial.png"))
    myImage3= ImageTk.PhotoImage(Image.open("images/transmissionCapacityFinal.png"))
    image_list = [myImage1,myImage2,myImage3]
    totalImages = len(image_list)
    current_image = 0
    next_image = 0
    prev_image = 0
    my_label = Label(outputFrame1,image=myImage1)
    my_label.grid(row=0,column=0, columnspan=2)
    button_back = Button(outputFrame1, text="<<", command=back, state=DISABLED)
    button_exit = Button(outputFrame1,text="EXIT",command=root.quit)
    button_forward = Button(outputFrame1,text=">>", command=forward)
    button_back.grid(row=1,column=0)
    # button_exit.grid(row=1,column=1)
    button_forward.grid(row=1, column=1)

root = Tk()
root.configure()
root.geometry("1440x900")
root.title("AI Assisted Energy Efficent Wirless Routing Algorithm")

inputFrame = LabelFrame(root,text="Input", padx=10,pady=10)
inputFrame.pack(padx=10,pady=10)
# inputFrame.grid(row=0,column=0)

outputFrame1 = LabelFrame(root,padx=10, pady=10,text="Output")
outputFrame1.pack(padx=10,pady=10)
# outputFrame1.grid(row=1, column=0)
# Creating Dropdown menu to select the network topolgy
options = ["pdh" , "COST266", "di-yuan"]

clicked = StringVar()
clicked.set("pdh")

topologyDropDown = OptionMenu(inputFrame, clicked, *options)
topolgySelectLabel = Label(inputFrame,text="Select Topology")
topolgySelectLabel.grid(row=0,column=0, padx=10, pady=10)
topologyDropDown.grid(row=0,column=1,padx=10,pady=10)

#Confirm button to run the algorithm on the code
confirmButton = Button(inputFrame,text="CONFIRM", fg="green",padx=20, pady=20, command=confirmButton)
confirmButton.grid(row=1,column=0)
#3 images. One before running the algorithm. The intial weights, final weights and 
# other metric

#Exit button
exitButton = Button(inputFrame,text= "EXIT", fg = "red",command=root.quit, padx=20, pady=20)
exitButton.grid(row=1,column=1)

root.mainloop()
    