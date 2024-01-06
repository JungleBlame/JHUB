import matplotlib.pyplot as plt

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
                making_inputs(File,route)


        except FileNotFoundError:
            print("File not found")
            route_path_func()

#---------------------------------------------------------------------------------------------------------------------------#

def making_inputs(File,route):
    """Gives starting coords and path"""

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

    check=0

    check=check_func(x_plots,check)
    check=check_func(y_plots,check)

    if check ==0:
        making_the_grid(x_plots,y_plots)

    else:

        print("The Route is outside of the grid")
        route_path_func()

#---------------------------------------------------------------------------------------------------------------------------#

def check_func(list_plots,check):
    """Func to check if plots are correct"""

    for plots in list_plots:
        if plots >12 or plots <0:
            check+=1

    return check

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

    coordinates= make_coordinates(x_plots,y_plots)
    print("Coordinates are: ", coordinates)

    plt.plot(x_plots, y_plots, marker="X")
    plt.grid()
    plt.show()

    route_path_func()

#---------------------------------------------------------------------------------------------------------------------------#

def stop_run():
    """Func to exit the function call"""

    print("Ok, stopping function.")
    return

#---------------------------------------------------------------------------------------------------------------------------#
#                                                        >Runner<

route_path_func()
