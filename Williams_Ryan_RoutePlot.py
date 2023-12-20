import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------------------------------------------------------------#

def route_path_func():
    """Func that prompts user for route path and enables stopping"""

    route = input("Please enter a route file name or STOP to end: ")
    
    if route.upper() == "STOP":
        stop_run()
    
    elif route.upper()!="STOP":

        try:
            with open(route, "r") as File:
                File=File.read()
                making_inputs(File)
            

        except FileNotFoundError:
            print("File not found")
            route_path_func()
        

#---------------------------------------------------------------------------------------------------------------------------#
            
def making_inputs(File):
    "Gives starting coords and path"

    coordinates=list(File)
   
    path=[]
    x_start=""
    y_start=""

    nums=['1','2','3','4','5','6','7','8','9','0']
    set=0
    for char in coordinates:
        if char in nums:

            if set==0:
                x_start+=char
            elif set==1:
                y_start+=char
        elif char== '\n':
            set=1
        else:
            path+=char

    x_plots=[int(x_start)]
    y_plots=[int(y_start)]
    X=int(x_start)
    Y=int(y_start)

    for directions in path:
        
        if directions=='N':
            x_plots.append(X) 
            Y=int(Y+1)
            y_plots.append(Y)
        
        elif directions=='S':
            x_plots.append(X)
            Y=int(Y-1)
            y_plots.append(Y)

        elif directions=='E':
            y_plots.append(Y)
            X=int(X+1)
            x_plots.append(X)

        elif directions=='W':
            y_plots.append(Y)
            X=int(X-1)
            x_plots.append(X)

    check_func(x_plots)
    check_func(y_plots)
    making_the_grid(x_plots,y_plots)

#---------------------------------------------------------------------------------------------------------------------------#                

def check_func(list_plots):
    """Func to check if plots are correct"""

    for plots in list_plots:
        if plots >12 or plots <0:
            print("The Route is outside of the grid")
            route_path_func()
    
#---------------------------------------------------------------------------------------------------------------------------#

def make_coordinates(x_plots,y_plots):
    """Func to return coordinates from x and y plots"""
    
    couple=[]
    coordinates=[]
    counter=len(x_plots)
    index=0

    while counter!=0:
        
        couple.append(x_plots[index])
        couple.append(y_plots[index])
        coordinates.append(couple)
        couple=[]
        index+=1
        counter-=1
    
    return coordinates
#---------------------------------------------------------------------------------------------------------------------------#

def making_the_grid(x_plots,y_plots):
    """Func to make the grid using np and plt"""
    
    xpoints = np.array(x_plots)
    ypoints = np.array(y_plots)

    plt.plot(xpoints, ypoints, marker="X")
    plt.grid()
    plt.show()
    
    coordinates= make_coordinates(x_plots,y_plots)
    print("Coordinates are: ", coordinates)


    route_path_func()

#---------------------------------------------------------------------------------------------------------------------------#

def stop_run():
    print("Ok, stopping")
    return

#---------------------------------------------------------------------------------------------------------------------------#
#                                                        >Runner<

route_path_func()
    
