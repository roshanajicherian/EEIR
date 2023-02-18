import sndlib_model
import os
demands_dict = sndlib_model.create_graph(f"{os.getcwd()}\\input\\pdh.txt")
print("Demands Dictionary : ", demands_dict)