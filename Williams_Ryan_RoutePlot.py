
def drone_func():

    route = input("Please enter a route file name or STOP to end: ")
    print(route)
    if route.upper() == "STOP":
        print("Ok, stopping")
        return 
    

    else:
        try:
            route=open(route, "r")
            coordinates=route.read()
            print(coordinates)
        except:
            print("File not found")
            drone_func()
    
    



drone_func()

