import matplotlib.pyplot as plt
import numpy as np


#---------------------------------------------------------------------------------------------------------------------------#

def route_path_func():
    """Func that prompts user for route path and enables stopping"""

    route = input("Please enter a route file name or STOP to end: ")
    
    if route.upper() == "STOP":
        print("Ok, stopping")
        return 
    
    else:
        try:
            route=open(route, "r")
            route=route.read()
            print(route)
            making_inputs(route)

        except:
            print("File not found")
            route_path_func()

#---------------------------------------------------------------------------------------------------------------------------#
def making_inputs(coordinates):
    "Gives starting coords and path"

    coordinates=list(coordinates)
   
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

    x_plots=[]
    y_plots=[]
    x_plots.append(int(x_start))
    y_plots.append(int(y_start))
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
    
    print(x_plots)
    print(y_plots)


    #making_the_grid(x_plots,y_plots)
#---------------------------------------------------------------------------------------------------------------------------#                
def making_the_grid(x_plots,y_plots):
    """Func to make the grid using np and plt"""
    
    x = x_plots
    y = y_plots
    





    plt.plot(x, y)
    plt.show()

    
#---------------------------------------------------------------------------------------------------------------------------#
#                                                        >Runner<

route_path_func()
#coordinates= open("Route001.txt", "r")
#coordinates=coordinates.read()
#making_inputs(coordinates)

#route = input("Please enter a route file name or STOP to end: ")

#route=open(route, "r")
#route=route.read()

