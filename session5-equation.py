import math

def Quadratic_Equation():

    print(" Welcome! You can solve your quadratic equations here! ")

    while True:
           
           userinput=("Enter your numbers for the equation: ")
           a=int(input("Enter  a: "))
           b=int(input("Enter  b:"))
           c=int(input("Enter  c: "))

           delta = b**2-4*a*c
           
           if delta > 0:
               x1 = (-b +math.sqrt(delta)) / (2*a)
               x2 = (-b -math.sqrt(delta)) / (2*a)
               print ("X1 =", x1,"  X2 =", x2)

           elif delta == 0 :
                x = -b / (2*a)
                print ("X =", x) 
           else :
                print(" !invalid! ")         


Quadratic_Equation()

