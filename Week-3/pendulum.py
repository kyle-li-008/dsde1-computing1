def period(L, g):
    from math import pi 
    T = ""
    L_input = isinstance(L, int)
    g_input = isinstance(g, int)
    print("L_input")
    print("g_input")
    if L_input != True:
        print("Wrong input")
    elif g_input != True:
        print("Wrong input")
    else:
        T = 2 * pi * (L/g)**(1/2)
        return T
        
    