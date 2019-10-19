def period(L, g):
    from math import pi 
    T = None
    L_input = isinstance(L, int)
    g_input = isinstance(g, int)
    print("L_input")
    print("g_input")
    if L_input != Ture:
        print("Wrong input")
    elif g_input != Ture:
        print("Wrong input")
    else:
        T = 2 * pi * (L/g)**(1/2)
        return T
        
    