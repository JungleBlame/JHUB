
def drone_func():

    route = input("Please enter a route file name or STOP to end: ")

    if route.upper() == "STOP":
        print("Ok, stopping")
        return 
    
    else:
        try:
            open(route, "r")
            coordinates=route.read()
        except:
            print ("File not found")
            drone_func()
    



drone_func()

