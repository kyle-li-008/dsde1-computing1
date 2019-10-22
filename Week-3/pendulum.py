def period(L, g):
    import math
    T = None
    L_input = isinstance(L, int)
    g_input = isinstance(g, int)
    print("L_input")
    print("g_input")
    if L_input != True:
        print("Wrong input")
    elif g_input != True:
        print("Wrong input")
    else:
        T = 2 * math.pi * (int(L)/int(g))**(1/2)
        return T

# print(period(4, 9))

    
#import my function as mf
#python name.py 

# def main():
#     period()

if __name__ == '__main__':
    L_int = input()
    g_int = input()
    L = int(L_int)
    g = int(g_int)
    period(L, g)
