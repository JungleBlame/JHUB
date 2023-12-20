import matplotlib.pyplot as plt
import numpy as np


#---------------------------------------------------------------------------------------------------------------------------#

def route_path_func():
    """Func that prompts user for route path and enables stopping"""

    route = input("Please enter a route file name or STOP to end: ")
    print(route)
    if route.upper() == "STOP":
        print("Ok, stopping")
        return 
    
    else:
        try:
            route=open(route, "r")
            coordinates=route.read()
            #print(coordinates)
            making_the_grid(coordinates)

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

    x_plots=list(int(x_start))
    y_plots=list(int(y_start))
    X=x_plots
    Y=y_plots

    for directions in path:
        
        if directions=='N':
            x_plots+= X 
            Y=Y+1
            y_plots+= Y
        
        elif directions=='S':
            x_plots+= X 
            Y=Y-1
            y_plots+= Y

        elif directions=='E':
            y_plots+= Y
            X=X+1
            x_plots+= X

        elif directions=='W':
            y_plots+= Y
            X=X-1
            x_plots+= X
    
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
    

    